#!/usr/bin/env python3
import socket
import re
HOST = "154.57.164.67"
PORT = 30500
def solve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(10)

    def recv_until_prompt():
        data = b""
        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
                if data.endswith(b"> "):
                    break
            except socket.timeout:
                break
        return data.decode("utf-8", errors="replace")

    intro = recv_until_prompt()
    print(intro)
    s.sendall(b"1\n")
    for rnd in range(100):
        output = recv_until_prompt()
        print(output)

        lines = output.split("\n")
        players_ordered = []
        for line in lines:
            m = re.match(r"Player\s+(\d+):\s+([\d\s]+)", line.strip())
            if m:
                player_num = int(m.group(1))
                dice = list(map(int, m.group(2).strip().split()))
                players_ordered.append((player_num, sum(dice)))
        if not players_ordered:
            print("[!] Could not parse player scores!")
            print(repr(output))
            break

        max_score = max(score for _, score in players_ordered)
        winner = max(player_num for player_num, score in players_ordered if score == max_score)
        print(f"  --> Round {rnd+1}: Winner = Player {winner} (score={max_score})")
        s.sendall(f"{winner}\n".encode())

    # Get the flag
    final = b""
    try:
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            final += chunk
    except:
        pass
    print("\n=== FINAL ===")
    print(final.decode("utf-8", errors="replace"))
    s.close()
if __name__ == "__main__":
    solve()