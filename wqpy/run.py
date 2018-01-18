# encoding: UTF-8

from wqpy.eventEngine import EventEngine
from wqpy.mainEngine import MainEngine

# 加载上层应用
from wqpy.app.strategy.strategyEngine import StrategyEngine
from wqpy.app.strategy.simulateStrategy import SimulateStrategy
from wqpy.tdApi.simulateTdApi import SimulateTdApi
from wqpy.mdApi.simulateMdApi import SimulateMdApi


def main():

    me = MainEngine()

    # add trading and market data api
    me.add_td_api(SimulateTdApi)
    me.add_md_api(SimulateMdApi)

    # add application
    me.add_app(StrategyEngine)
    se = me.get_app('Strategy')

    # start strategy application
    se.start()
    me.exit(0.1)


if __name__ == '__main__':
    main()
