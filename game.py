import random

class Player:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.hand = []

class Game:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.players = []
        self.deck = []
        self.started = False

    def add_player(self, user_id, name):
        if any(p.id == user_id for p in self.players):
            return f"{name} 已经在游戏中"
        self.players.append(Player(user_id, name))
        return f"{name} 加入了游戏。当前玩家数：{len(self.players)}"

    def deal_cards(self):
        if len(self.players) < 2:
            return "需要至少 2 个玩家才能开始游戏"
        self.started = True
        self.deck = self._create_deck()
        random.shuffle(self.deck)
        for player in self.players:
            player.hand = [self.deck.pop(), self.deck.pop()]
        msg = "发牌完成，每位玩家已收到两张手牌。\n"
        for p in self.players:
            msg += f"{p.name} 手牌：{p.hand}\n"
        return msg

    def _create_deck(self):
        suits = ['♠', '♥', '♦', '♣']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [v + s for v in values for s in suits]

def start_new_game(chat_id):
    return Game(chat_id)

def handle_player_action(game, user_id, action):
    player = next((p for p in game.players if p.id == user_id), None)
    if not player:
        return "你不在游戏中"

    if action == "fold":
        return f"{player.name} 弃牌"
    elif action == "call":
        return f"{player.name} 跟注"
    elif action == "raise":
        return f"{player.name} 加注"
    return "未知操作"