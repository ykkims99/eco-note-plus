from datetime import datetime
with open("docs/generated_log.txt", "w") as f:
    f.write("Eco-Note+ 시스템 로그\n")
    f.write("기록 시각: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
