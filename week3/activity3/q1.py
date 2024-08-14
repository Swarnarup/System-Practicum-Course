from pythonping import ping

# tst = ping('8.8.8.8', size=40, count=10)

tst = ping('8.8.8.8', sweep_start=100, sweep_end=1000, df=True)

print(tst.rtt_avg_ms)