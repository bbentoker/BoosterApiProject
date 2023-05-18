import psycopg2
from config import *
from validations.lol_validation import RankBoost, DuoBoost, WinBoost, PlacementsBoost, NormalBoost

class VALORANT_CRUD:
    def create_rank_boost(self,rank_boost: RankBoost):
        conn = psycopg2.connect(
        host=DB_HOSTNAME,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO valorant (user_id, order_type,current_rank, current_rr, server, desired_rank, q_type, priority_boost, stream_games, solo_only, bonus_win, total_price) VALUES (%s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (rank_boost.user_id,rank_boost.order_type, rank_boost.current_rank, rank_boost.current_lp, rank_boost.server, rank_boost.desired_rank, rank_boost.q_type, rank_boost.priority_boost, rank_boost.stream_games, rank_boost.solo_only, rank_boost.bonus_win, rank_boost.total_price))
        conn.commit()

        cur.close()
        conn.close()

    def create_win_boost(self,win_boost: WinBoost):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO valorant (user_id,order_type, current_rank, server, wins_amount, q_type, play_with_booster, priority_boost, stream_games, solo_only, total_price) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (win_boost.user_id,win_boost.order_type, win_boost.current_rank, win_boost.server, win_boost.wins_amount, win_boost.q_type, win_boost.play_with_booster, win_boost.priority_boost, win_boost.stream_games, win_boost.solo_only, win_boost.total_price))
        conn.commit()

        cur.close()
        conn.close()   
    def create_duo_boost(self,duo_boost: DuoBoost):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO valorant (user_id,order_type, current_rank, current_rr, server, desired_rank, q_type, champions_roles, priority_boost, bonus_win, total_price) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (duo_boost.user_id,duo_boost.order_type, duo_boost.current_rank, duo_boost.current_lp, duo_boost.server, duo_boost.desired_rank, duo_boost.q_type, duo_boost.champions_roles, duo_boost.priority_boost, duo_boost.bonus_win, duo_boost.total_price))
        conn.commit()

        cur.close()
        conn.close()        


    def create_placement_boost(self, placement_boost: PlacementsBoost):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO valorant (user_id,order_type, previous_rank, server, q_type, wins_amount, play_with_booster,  priority_boost, stream_games, solo_only, total_price) VALUES (%s,%s, %s,%s, %s, %s, %s, %s, %s, %s, %s)", (placement_boost.user_id,placement_boost.order_type, placement_boost.previous_rank, placement_boost.server, placement_boost.q_type, placement_boost.wins_amount, placement_boost.play_with_booster, placement_boost.priority_boost, placement_boost.stream_games, placement_boost.solo_only, placement_boost.total_price))
        conn.commit()

        cur.close()
        conn.close()

    def create_normal_boost(self,normal_boost: NormalBoost):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO valorant (user_id,order_type, games_amount, game_mode, server, play_with_booster, priority_boost, stream_games, solo_only, total_price) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)", (normal_boost.user_id,normal_boost.order_type, normal_boost.games_amount, normal_boost.game_mode, normal_boost.server, normal_boost.play_with_booster, normal_boost.priority_boost, normal_boost.stream_games, normal_boost.solo_only, normal_boost.total_price))
        conn.commit()

        cur.close()
        conn.close()






  


