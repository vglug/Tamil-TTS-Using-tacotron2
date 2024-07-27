""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_tamil_letters = 'அ, ஆ, இ, ஈ, உ, ஊ, எ, ஏ, ஐ, ஒ, ஓ, ஔ, க, கா, கி, கீ, கு, கூ, கெ, கே, கை, கொ, கோ, கௌ, ங, ஙா, ஙி, ஙீ, ஙு, ஙூ, ஙெ, ஙே, ஙை, ஙொ, ஙோ, ஙௌ, ச, சா, சி, சீ, சு, சூ, செ, சே, சை, சொ, சோ, சௌ,ஞ, ஞா, ஞி, ஞீ, ஞு, ஞூ, ஞெ, ஞே, ஞை, ஞொ, ஞோ, ஞௌ, ட, டா, டி, டீ, டு, டூ, டெ, டே, டை, டொ, டோ, டௌ,ண, ணா, ணி, ணீ, ணு, ணூ, ணெ, ணே, ணை, ணொ, ணோ, ணௌ,த, தா, தி, தீ, து, தூ, தெ, தே, தை, தொ, தோ, தௌ,ந, நா, நி, நீ, நு, நூ, நெ, நே, நை, நொ, நோ, நௌ,ப, பா, பி, பீ, பு, பூ, பெ, பே, பை, பொ, போ, பௌ,ம, மா, மி, மீ, மு, மூ, மெ, மே, மை, மொ, மோ, மௌ,ய, யா, யி, யீ, யு, யூ, யெ, யே, யை, யொ, யோ, யௌ,ர, ரா, ரி, ரீ, ரு, ரூ, ரெ, ரே, ரை, ரொ, ரோ, ரௌ,ல, லா, லி, லீ, லு, லூ, லெ, லே, லை, லொ, லோ, லௌ,வ, வா, வி, வீ, வு, வூ, வெ, வே, வை, வொ, வோ, வௌ,ழ, ழா, ழி, ழீ, ழு, ழூ, ழெ, ழே, ழை, ழொ, ழோ, ழௌ,ள, ளா, ளி, ளீ, ளு, ளூ, ளெ, ளே, ளை, ளொ, ளோ, ளௌ,ற, றா, றி, றீ, று, றூ, றெ, றே, றை, றொ, றோ, றௌ,ன, னா, னி, நீ, நு, நூ, நெ, நே, நை, நொ, நோ, நௌ,ஃ,க்,ங்,ச்,ஞ்,ட்,ண்,த்,ந்,ப்,ம்,ய்,ர்,ல்,வ்,ழ்,ள்,ற்,ன்,ஷ, ஷா, ஷி, ஷீ, ஷு, ஷூ, ஷெ, ஷே, ஷை, ஷொ, ஷோ, ஷௌ,ஸ, ஸா, ஸி, ஸீ, ஸு, ஸூ, ஸெ, ஸே, ஸை, ஸொ, ஸோ, ஸௌ,ஹ, ஹா, ஹி, ஹீ, ஹு, ஹூ, ஹெ, ஹே, ஹை, ஹொ, ஹோ, ஹௌ,க்ஷ, க்ஷா, க்ஷி, க்ஷீ, க்ஷு, க்ஷூ, க்ஷெ, க்ஷே, க்ஷை, க்ஷொ, க்ஷோ, க்ஷௌ,ஜ, ஜா, ஜி, ஜீ, ஜு, ஜூ, ஜெ, ஜே, ஜை, ஜொ, ஜோ, ஜௌ'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet + _tamil_letters.split(',')
