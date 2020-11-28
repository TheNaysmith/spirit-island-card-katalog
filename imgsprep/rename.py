#!/usr/bin/env python3

import glob, os
from fuzzywuzzy import process

# generated with:
# "[" + CARDS.filter((c) => c instanceof Types.PowerCard).map((c) => '"' + c.getImagePath().substring(12) + '"').join(", ") + "]"
powers = ["shatter_homesteads", "raging_storm", "lightnings_boon", "harbingers_of_the_lightning", "flash_floods", "wash_away", "boon_of_vigor", "rivers_bounty", "concealing_shadows", "favors_called_due", "mantle_of_dread", "crops_wither_and_fade", "guard_the_healing_land", "a_year_of_perfect_stillness", "rituals_of_destruction", "draw_of_the_fruitful_earth", "manifestation_of_power_and_glory", "words_of_warning", "sudden_ambush", "voice_of_thunder", "call_of_the_deeps", "grasping_tide", "swallow_the_landdwellers", "tidal_boon", "predatory_nightmares", "dread_apparitions", "call_on_midnights_dreams", "dreams_of_the_dahan", "overgrow_in_a_night", "gift_of_proliferation", "fields_choked_with_growth", "stem_the_flow_of_fresh_water", "savage_mawbeasts", "voracious_growth", "rouse_the_trees_and_stones", "encompassing_ward", "song_of_sanctity", "uncanny_melting", "shadows_of_the_burning_forest", "steam_vents", "veil_the_nights_hunt", "elemental_boon", "devouring_ants", "dark_and_tangled_woods", "sap_the_strength_of_multitudes", "drift_down_into_slumber", "land_of_haunts_and_embers", "natures_resilience", "visions_of_fiery_doom", "pull_beneath_the_hungry_earth", "call_of_the_dahan_ways", "call_to_bloodshed", "call_to_isolation", "call_to_migrate", "call_to_tend", "quicken_the_earths_struggles", "delusions_of_danger", "drought", "gift_of_constancy", "enticing_splendor", "entrancing_apparitions", "gift_of_living_energy", "gift_of_power", "gnawing_rootbiters", "lure_of_the_unknown", "purifying_flame", "rain_of_blood", "reaching_grasp", "accelerated_rot", "cleansing_floods", "pillar_of_living_flame", "poisoned_land", "terrifying_nightmares", "the_trees_and_stones_speak_of_war", "entwined_power", "paralyzing_fright", "powerstorm", "talons_of_lightning", "the_jungle_hungers", "the_land_thrashes_in_furious_pain", "tsunami", "vigor_of_the_breaking_dawn", "vengeance_of_the_dead", "wrap_in_wings_of_sunlight", "blazing_renewal", "winds_of_rust_and_atrophy", "indomitable_claim", "mists_of_oblivion", "infinite_vitality", "dissolve_the_bonds_of_kinship", "strangling_firevine", "bloodwrack_plague", "cast_down_into_the_briny_deep", "death_falls_gently_from_open_blossoms", "fire_and_flood", "grant_hatred_a_ravenous_form", "insatiable_hinger_of_the_swarm", "instruments_of_their_own_ruin", "flow_like_water_reach_like_air", "pentup_calamity", "pyroclastic_flow", "savage_transformation", "sea_monsters", "tigers_hunting", "unrelenting_growth", "volcanic_eruption", "sweep_into_the_sea", "manifest_incarnation", "smothering_infestation", "twisted_flowers_murmur_ultimatums", "unlock_the_gates_of_deepest_power", "inflame_the_fires_of_life", "fire_in_the_sky", "fleshrot_fever", "golds_allure", "guardian_serpents", "here_there_be_monsters", "infested_aquifers", "poisoned_dew", "portents_of_disaster", "prowling_panthers", "renewing_rain", "rites_of_the_lands_rejection", "pact_of_the_joined_hunt", "razorsharp_undergrowth", "growth_through_sacrifice", "scour_the_land", "sky_stretches_to_shore", "swarming_wasps", "absorb_corruption", "animated_wrackroot", "promises_of_protection", "call_to_ferocity", "call_to_trade", "confounding_mists", "cycles_of_time_and_tide", "disorienting_landscape", "elusive_ambushes", "tormenting_rotflies", "twilight_fog_brings_madness", "teeming_rivers", "spur_on_with_words_of_fire", "prey_on_the_builders", "teeth_gleam_from_darkness", "too_near_the_jungle", "terrifying_chase", "towering_wrath", "regrow_from_roots", "boon_of_growing_power", "sacrosanct_wilderness", "flashfires", "asphyxiating_smoke", "flames_fury", "threatening_flames", "gift_of_the_primordial_deeps", "gift_of_flowing_power", "absorb_essence", "elemental_aegis"]
# generated with:
# "[" + CARDS.filter((c) => c instanceof Types.FearCard).map((c) => '"' + c.getImagePath().substring(11) + '"').join(", ") + "]"
fears = ["fear_of_the_unseen", "scapegoats", "emigration_accelerates", "dahan_on_their_guard", "tall_tales_of_savagery", "retreat", "dahan_raid", "dahan_enheartened", "avoid_the_dahan", "seek_safety", "wary_of_the_interior", "belief_takes_root", "isolation", "overseas_trade_seems_safer", "trade_suffers", "demoralized", "plan_for_departure", "tread_carefully", "dahan_attack", "explorers_are_reluctant", "immigration_slows", "flee_the_pestilent_land", "quarantine", "too_many_monsters", "panicked_by_wild_beasts", "depart_the_dangerous_land", "unrest", "panic", "discord", "dahan_threaten"]

# generated with:
# "[" + CARDS.filter((c) => c instanceof Types.EventCard).map((c) => '"' + c.getImagePath().substring(12) + '"').join(", ") + "]"
events = ["years_of_little_rain", "farmers_seek_the_dahan_for_aid", "new_species_spread", "war_touches_the_islands_shores", "sacred_sites_under_threat", "outpaced", "missionaries_arrive", "a_strange_madness_among_the_beasts", "seeking_the_interior", "wave_of_reconnaissance", "interesting_discoveries", "strange_tales_attract_explorers", "cultural_assimilation", "investigation_of_dangers", "distant_exploration", "rising_interest_in_the_island", "putting_down_roots", "search_for_new_lands", "invaders_surge_inland", "tightknit_communities", "wellprepared_explorers", "population_rises", "urban_development", "heavy_farming", "promising_farmland", "slave_rebellion"]

if not os.path.isdir("powers/"):
    os.mkdir("powers/")
if not os.path.isdir("fears/"):
    os.mkdir("fears/")
if not os.path.isdir("events/"):
    os.mkdir("events/")

with open("ocr.txt") as f:
    content = f.readlines()

content = [line.split()[0:2] for line in content]
for card in content:
    if len(card) == 2:
        [file, ocr] = card
        if len(powers) == 0:
            (power, powerrating) = ("EMPTY", 0)
        else:
            (power, powerrating) = process.extractOne(ocr, powers)
        if len(fears) == 0:
            (fear, fearrating) = ("EMPTY", 0)
        else:
            (fear, fearrating) = process.extractOne(ocr, fears)
        if len(events) == 0:
            (event, eventrating) = ("EMPTY", 0)
        else:
            (event, eventrating) = process.extractOne(ocr, events)
        if powerrating > 70:
            powers.remove(power)
            os.rename(file + ".webp", "powers/" + power + ".webp")
            os.rename(file + ".jpg", "powers/" + power + ".jpg")
        elif fearrating > 70:
            fears.remove(fear)
            os.rename(file + ".webp", "fears/" + fear + ".webp")
            os.rename(file + ".jpg", "fears/" + fear + ".jpg")
        elif eventrating > 70:
            events.remove(event)
            os.rename(file + ".webp", "events/" + event + ".webp")
            os.rename(file + ".jpg", "events/" + event + ".jpg")
        else:
            print("NOT MATCHED: ", power, fear, ocr, file)
if len(powers) > 0:
    print("POWERS NOT EMPTY: ", powers)
if len(fears) > 0:
    print("FEARS NOT EMPTY: ", fears)
if len(events) > 0:
    print("EVENTS NOT EMPTY: ", events)
