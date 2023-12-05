def time_to_text(x: int) -> None:
    h, m= x // 60, x % 60
    print(f"{h} heures et {m} minutes")


time_to_text(49)
time_to_text(60)
time_to_text(890)