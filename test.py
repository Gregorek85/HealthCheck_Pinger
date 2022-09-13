from HealthCheck_Pinger import pingDecor
from time import sleep


@pingDecor("uuid")
def myTest():
    print("Start")
    sleep(5)
    print("End")


myTest()
