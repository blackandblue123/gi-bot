import pandas as pd
import numpy as np

file_path = 'genshin_data.xlsx'

char_cols = [
    'Character', 'Element', 'Weapon Type', 'Base ATK', 'Rarity', 'URL',
]

weapon_cols = [
    'Weapon', 'Rarity', 'Type', 'Base ATK', 'Substat', 'URL', 'Passive',
]

artifact_cols = [
    'Set', 'Rarity', 'URL', 'From', '2-Piece Bonus', '4-Piece Bonus',
]

character_df = pd.read_excel(
    file_path,
    sheet_name="Characters",
    usecols=char_cols,
).dropna().rename(columns={
    'Character': 'name',
    'Element': 'element',
    'Weapon Type': 'weapon_type',
    'Base ATK': 'base_atk',
    'Rarity': 'rarity',
    'URL': 'icon_url',
})

weapon_df = pd.read_excel(
    file_path,
    sheet_name="Weapons",
    usecols=weapon_cols,
).dropna().rename(columns={
    'Weapon': 'name',
    'Substat': 'substat',
    'Type': 'type',
    'Base ATK': 'base_atk',
    'Rarity': 'rarity',
    'URL': 'icon_url',
    'Passive': 'passive',
})

artifact_df = pd.read_excel(
    file_path,
    sheet_name="Artifacts",
    usecols=artifact_cols,
).dropna().rename(columns={
    'Set': 'name',
    'Rarity': 'rarity',
    'From': 'where',
    '2-Piece Bonus': 'two_piece_effect',
    '4-Piece Bonus': 'four_piece_effect',
    'URL': 'icon_url',
})
