invite_userid = 1800438

import requests

sids = [
    "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
    "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
    "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
    "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
    "V02ScVbtm2pQD49ArcgGLv360iqQFLs014c8062e000b6c37b6",
    "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
    "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
    "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
    "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
    "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
    "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d",
    "c185ca410ea7eec31590507fc6bd53b91e8a46bd000b6645b8",
    "1f19b469b864819bc6f6ccab5dadc12f4fc3e8f9000c75bf55",
    "3ca9bd94a644a44956a7cb5db56c00ee96c4b1840000b39aab",
    "b6ddffa0b1eed41ebdf322b1810166299fb236ec000c5c57d8",
    "0f986dff4c9c5013f24be07082d34436a21ac6bc000c18a129",
    "5a58420c49eaae6ee786222b33241973759a841a000c7487f1",
    "3cb5edc22ed922931f96bbbc396262b574896acd000c536a31",
    "acc1ad45beaaa431c2fa6a02af274bb23892de17000c30ca3f"
]

invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
for i in sids:
    requests.post(invite_url, headers={'sid': i}, data={'invite_userid': invite_userid})
    
