def should_hit(player_total, dealer_card_val, player_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay. player_aces is the number of aces the player has.
    """
	if player_total in [4,5,6,7,8,9,10]:
		return True
	elif player_aces == 1 and player_total in [12,13,14,15,16,17]: #soft12-17
		return True
	elif player_aces == 1 and player_total == 18 and dealer_card_val not in [2,3,4,5,6,7,8]: #soft18
		return True
	elif player_total == 11: #hard11
			return True
	elif player_total == 12 and dealer_card_val not in [4,5,6]: #hard12
		if player_aces == 0 or player_aces > 1:
			return True
		else:
			return False
	elif player_total in [13,14,15,16] and dealer_card_val not in [2,3,4,5,6]:
		if player_aces == 0 or player_aces > 1:
			return True #hard13,14,15,16
		else:
			return False
		
    return False