from matplotlib import pyplot as plt
from pymongo import *
from io import BytesIO
from datetime import datetime
import matplotlib.dates as mdates


class Graph:
    def __init__(self, client):
        self.client = client
        self.plt = plt
        self.companies = self.get_companies()
        self.dates = self.get_dates()
        self.refresh()

    def get_companies(self):
        db = self.client.LotteryBot

        coll = db.stockValue

        docs = coll.find().sort("_id", ASCENDING)
        companies = {}
        for doc in docs:
            if not doc["company"] in companies:
                companies[doc["company"]] = []
            companies[doc["company"]].append(doc["value"])
        return companies

    def get_company(self, company):
        return self.companies[company]

    def refresh(self):
        self.companies = self.get_companies()
        self.dates = self.get_dates()

    def render_graph(self, mark_last=True):
        self.plt.cla()
        self.plt.clf()
        company_colors = {
            "Lottery Inc.": "gold",
            "Photon Corp.": "royalblue",
            "SolarFox Ent.": "darkorange"
        }
        yt = []
        c = 1
        for company in self.companies:
            values = self.companies[company]
            markers = None
            yt.append(values[-1])
            if mark_last:
                ax = self.plt.gca().secondary_yaxis("right")
                markers = [-1]
                ax.set_ticks(yt)
            self.plt.plot(self.dates, values, 'o', ls='-', ms=4, markevery=markers, c=company_colors[company],
                          label="({}) {}".format(c, company))
            c += 1
        self.plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
        self.plt.grid(True)
        self.plt.legend()

    def to_bytes(self, f="png"):
        buffer = BytesIO()
        self.plt.savefig(buffer, format=f)
        return buffer

    def get_plt(self):
        return self.plt

    def get_dates(self):
        companies = self.get_companies()
        db = self.client.LotteryBot

        coll = db.stockValue

        docs = coll.find({"company": next(iter(companies))})
        dates = []
        for doc in docs:
            dates.append(datetime.strptime(doc["time"], "%Y-%m-%d %H:%M:%S"))
        return dates


print("-----------------------------------------")
print("    ____     __           ____        ")
print("   / __/__  / /__ _____  / __/__ __ __")
print("  _\\ \\/ _ \\/ / _ `/ __/ / _// _ \\ \\ /")
print(" /___/\\___/_/\\_,_/_/   /_/  \\___/_\\_\\ ")
print("> Lottery Graph System loaded !")
print("© 2021-Present, Solar Fox Entertainment")
print("-----------------------------------------")
