from random import randint

from db import connection_context
from models import Challenge, User

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    cpf varchar(16) UNIQUE NOT NULL,
    email varchar(100) UNIQUE NOT NULL,
    birth_date varchar(12) NOT NULL,
    phone_number varchar(20) NOT NULL
);
"""


CREATE_TABLE_CHALLENGE = """
CREATE TABLE IF NOT EXISTS challenges (
    id integer PRIMARY KEY,
    title varchar(100),
    score integer NOT NULL,
    user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);
"""

CLEAR_TABLE_CHALLENGE = "DELETE FROM challenges"

USER_DATA = [
User(111,email="111@gmail.com",cpf="111.111.111-111"),
User(112,email="112@gmail.com",cpf="112.112.112-112"),
User(113,email="113@gmail.com",cpf="113.113.113-113"),
User(114,email="114@gmail.com",cpf="114.114.114-114"),
User(115,email="115@gmail.com",cpf="115.115.115-115"),
User(116,email="116@gmail.com",cpf="116.116.116-116"),
User(117,email="117@gmail.com",cpf="117.117.117-117"),
User(118,email="118@gmail.com",cpf="118.118.118-118"),
User(119,email="119@gmail.com",cpf="119.119.119-119"),
User(120,email="120@gmail.com",cpf="120.120.120-120"),
User(121,email="121@gmail.com",cpf="121.121.121-121"),
User(122,email="122@gmail.com",cpf="122.122.122-122"),
User(123,email="123@gmail.com",cpf="123.123.123-123"),
User(124,email="124@gmail.com",cpf="124.124.124-124"),
User(125,email="125@gmail.com",cpf="125.125.125-125"),
User(126,email="126@gmail.com",cpf="126.126.126-126"),
User(127,email="127@gmail.com",cpf="127.127.127-127"),
User(128,email="128@gmail.com",cpf="128.128.128-128"),
User(129,email="129@gmail.com",cpf="129.129.129-129"),
User(130,email="130@gmail.com",cpf="130.130.130-130"),
User(131,email="131@gmail.com",cpf="131.131.131-131"),
User(132,email="132@gmail.com",cpf="132.132.132-132"),
User(133,email="133@gmail.com",cpf="133.133.133-133"),
User(134,email="134@gmail.com",cpf="134.134.134-134"),
User(135,email="135@gmail.com",cpf="135.135.135-135"),
User(136,email="136@gmail.com",cpf="136.136.136-136"),
User(137,email="137@gmail.com",cpf="137.137.137-137"),
User(138,email="138@gmail.com",cpf="138.138.138-138"),
User(139,email="139@gmail.com",cpf="139.139.139-139"),
User(140,email="140@gmail.com",cpf="140.140.140-140"),
User(141,email="141@gmail.com",cpf="141.141.141-141"),
User(142,email="142@gmail.com",cpf="142.142.142-142"),
User(143,email="143@gmail.com",cpf="143.143.143-143"),
User(144,email="144@gmail.com",cpf="144.144.144-144"),
User(145,email="145@gmail.com",cpf="145.145.145-145"),
User(146,email="146@gmail.com",cpf="146.146.146-146"),
User(147,email="147@gmail.com",cpf="147.147.147-147"),
User(148,email="148@gmail.com",cpf="148.148.148-148"),
User(149,email="149@gmail.com",cpf="149.149.149-149"),
User(150,email="150@gmail.com",cpf="150.150.150-150"),
User(151,email="151@gmail.com",cpf="151.151.151-151"),
User(152,email="152@gmail.com",cpf="152.152.152-152"),
User(153,email="153@gmail.com",cpf="153.153.153-153"),
User(154,email="154@gmail.com",cpf="154.154.154-154"),
User(155,email="155@gmail.com",cpf="155.155.155-155"),
User(156,email="156@gmail.com",cpf="156.156.156-156"),
User(157,email="157@gmail.com",cpf="157.157.157-157"),
User(158,email="158@gmail.com",cpf="158.158.158-158"),
User(159,email="159@gmail.com",cpf="159.159.159-159"),
User(160,email="160@gmail.com",cpf="160.160.160-160"),
User(161,email="161@gmail.com",cpf="161.161.161-161"),
User(162,email="162@gmail.com",cpf="162.162.162-162"),
User(163,email="163@gmail.com",cpf="163.163.163-163"),
User(164,email="164@gmail.com",cpf="164.164.164-164"),
User(165,email="165@gmail.com",cpf="165.165.165-165"),
User(166,email="166@gmail.com",cpf="166.166.166-166"),
User(167,email="167@gmail.com",cpf="167.167.167-167"),
User(168,email="168@gmail.com",cpf="168.168.168-168"),
User(169,email="169@gmail.com",cpf="169.169.169-169"),
User(170,email="170@gmail.com",cpf="170.170.170-170"),
User(171,email="171@gmail.com",cpf="171.171.171-171"),
User(172,email="172@gmail.com",cpf="172.172.172-172"),
User(173,email="173@gmail.com",cpf="173.173.173-173"),
User(174,email="174@gmail.com",cpf="174.174.174-174"),
User(175,email="175@gmail.com",cpf="175.175.175-175"),
User(176,email="176@gmail.com",cpf="176.176.176-176"),
User(177,email="177@gmail.com",cpf="177.177.177-177"),
User(178,email="178@gmail.com",cpf="178.178.178-178"),
User(179,email="179@gmail.com",cpf="179.179.179-179"),
User(180,email="180@gmail.com",cpf="180.180.180-180"),
User(181,email="181@gmail.com",cpf="181.181.181-181"),
User(182,email="182@gmail.com",cpf="182.182.182-182"),
User(183,email="183@gmail.com",cpf="183.183.183-183"),
User(184,email="184@gmail.com",cpf="184.184.184-184"),
User(185,email="185@gmail.com",cpf="185.185.185-185"),
User(186,email="186@gmail.com",cpf="186.186.186-186"),
User(187,email="187@gmail.com",cpf="187.187.187-187"),
User(188,email="188@gmail.com",cpf="188.188.188-188"),
User(189,email="189@gmail.com",cpf="189.189.189-189"),
User(190,email="190@gmail.com",cpf="190.190.190-190"),
User(191,email="191@gmail.com",cpf="191.191.191-191"),
User(192,email="192@gmail.com",cpf="192.192.192-192"),
User(193,email="193@gmail.com",cpf="193.193.193-193"),
User(194,email="194@gmail.com",cpf="194.194.194-194"),
User(195,email="195@gmail.com",cpf="195.195.195-195"),
User(196,email="196@gmail.com",cpf="196.196.196-196"),
User(197,email="197@gmail.com",cpf="197.197.197-197"),
User(198,email="198@gmail.com",cpf="198.198.198-198"),
User(199,email="199@gmail.com",cpf="199.199.199-199"),
User(200,email="200@gmail.com",cpf="200.200.200-200"),

]

MIN_CHALLENGES_PER_USER = 100
MAX_CHALLENGES_PER_USER = 600


def start_database():
    with connection_context() as cur:
        cur.execute(CREATE_TABLE_USER)
        cur.execute(CREATE_TABLE_CHALLENGE)
        cur.execute(CLEAR_TABLE_CHALLENGE)

        for user in USER_DATA:
            insert_cmd = f"""
                INSERT INTO users (id, email, cpf, birth_date, phone_number)
                VALUES (
                    {user.id},
                    '{user.email}',
                    '{user.cpf}',
                    '{user.birth_date}',
                    '{user.phone_number}'
                )
                ON CONFLICT DO NOTHING
            """
            cur.execute(insert_cmd)

            challenges_count = randint(
                MIN_CHALLENGES_PER_USER,
                MAX_CHALLENGES_PER_USER,
            )
            CHAR_A_OFFSET = 65
            for i in range(CHAR_A_OFFSET, challenges_count + CHAR_A_OFFSET):
                challenge = Challenge(user.id, f"Challenge {chr(i)}")
                insert_cmd = f"""
                    INSERT INTO challenges (title, score, user_id)
                    VALUES (
                        '{challenge.title}',
                        {challenge.score},
                        {challenge.user_id}
                    )
                    ON CONFLICT DO NOTHING
                """
                cur.execute(insert_cmd)
