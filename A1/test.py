import juran94


if __name__ =='__main__':
    agent = juran94
    print(agent.introduce())
    while True:
        temp = input()
        print(agent.respond(temp))
