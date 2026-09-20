"""
Seeds the 25-challenge matrix.
Hint policy (enforced by hint_linter.py):
  - easy/medium: hints may reference tools/techniques directly.
  - hard/insane: hints MUST be abstract riddles/lore — no tool names, no command
    syntax, no direct algorithm names. They should require human lateral thinking,
    not something an LLM can pattern-match into a working command.
"""
import hashlib
import db
from db import get_conn

def h(flag):
    return hashlib.sha256(flag.strip().encode()).hexdigest()

CHALLENGES = [
    # --- fully built samples ---
    dict(slug="witchs-ledger", title="The Witch's Ledger", category="Web Exploitation",
         difficulty="easy", points=80,
         description="A guest portal into the coven's ledger. Guests see nothing of value... or do they?\n"
                      "Target: standalone_challenges/witchs_ledger (deploy separately, see README).",
         flag=h("TOH{c00k13s_l13_3v3ry_h4ll0w_3v3}"),
         hint1="Cookies are just claims a browser makes about itself — nothing stops you from making a different claim.",
         hint2="Inspect what identifies your 'role' client-side, and ask what happens if you simply disagree with it.",
         is_active=1),

    dict(slug="covens-triple-curse", title="The Coven's Triple Curse", category="Cryptography",
         difficulty="medium", points=250,
         description="Three witches wove three layers of protection around the true name of the beast.\n"
                      "Ciphertext: =03MsBTbfhWZzY2cuNDcfNjcp9lcw81MtdGar91Myl2eUlUS",
         flag=h("TOH{th3_curs3_0f_th3_h3adl3ss_c0d3}"),
         hint1="The witches wove backwards, then hid it in plain (base64) sight, before the final enchantment.",
         hint2="The final layer's key is a Halloween staple — orange, carved, and glowing.",
         is_active=1),

    dict(slug="cursed-jackolantern", title="The Cursed Jack-o'-Lantern", category="Digital Forensics",
         difficulty="hard", points=480,
         description="A photograph was left on the porch. Something rides along with the light.",
         flag=h("TOH{c4rv1ng_pumpk1ns_r3v3417s_s3cr3ts}"),
         # Hard tier: riddle-style hints only, per policy — no tool/command names.
         hint1="The image remembers more than it shows. What is appended after a picture has finished being a picture?",
         hint2="The lock's name is spoken backwards in a language of thirteen letters, hiding a year the porch light "
               "first flickered, and the shape of what grows in October fields.",
         is_active=1),

    # --- placeholders: fill in real content before the event ---
    dict(slug="covens-welcome-scroll", title="The Coven's Welcome Scroll", category="General Skills",
         difficulty="easy", points=50, description="TODO: orientation/rules challenge.",
         flag=h("TOH{PLACEHOLDER_1}"), hint1="Read the rules page.", hint2="Check the Discord pins.", is_active=0),
    dict(slug="sign-the-guestbook", title="Sign the Guestbook", category="General Skills",
         difficulty="easy", points=50, description="TODO: social/OSINT warmup.",
         flag=h("TOH{PLACEHOLDER_2}"), hint1="Follow the club's socials.", hint2="Look at pinned posts.", is_active=0),
    dict(slug="whispers-through-veil", title="Whispers Through the Veil", category="Cryptography",
         difficulty="easy", points=60, description="TODO: Caesar/ROT13 puzzle.",
         flag=h("TOH{PLACEHOLDER_3}"), hint1="Rotate the letters.", hint2="Try 13.", is_active=0),
    dict(slug="bones-in-base64", title="Bones in Base64", category="Cryptography",
         difficulty="easy", points=70, description="TODO: layered encodings.",
         flag=h("TOH{PLACEHOLDER_4}"), hint1="Decode once.", hint2="Decode again.", is_active=0),
    dict(slug="trick-or-treat-tags", title="Trick-or-Treat Tags", category="Web Exploitation",
         difficulty="easy", points=60, description="TODO: hidden dir/HTML comment.",
         flag=h("TOH{PLACEHOLDER_5}"), hint1="View page source.", hint2="Check robots.txt.", is_active=0),
    dict(slug="polaroid-from-crypt", title="Polaroid from the Crypt", category="Digital Forensics",
         difficulty="easy", points=70, description="TODO: basic EXIF.",
         flag=h("TOH{PLACEHOLDER_6}"), hint1="Check image metadata.", hint2="Look at GPS/comment fields.", is_active=0),
    dict(slug="jack-o-lsb-tern", title="Jack-o'-LSB-tern", category="Steganography",
         difficulty="easy", points=80, description="TODO: LSB image stego.",
         flag=h("TOH{PLACEHOLDER_7}"), hint1="Least significant bits hide more than noise.", hint2="Try a stego extraction tool.", is_active=0),
    dict(slug="decompile-candy-counter", title="Decompile the Candy Counter", category="Reverse Engineering",
         difficulty="easy", points=90, description="TODO: strings/intro reversing.",
         flag=h("TOH{PLACEHOLDER_8}"), hint1="Run strings on the binary.", hint2="Look for a comparison function.", is_active=0),
    dict(slug="scavengers-riddle", title="The Scavenger's Riddle", category="Miscellaneous",
         difficulty="easy", points=100, description="TODO: puzzle/OSINT.",
         flag=h("TOH{PLACEHOLDER_9}"), hint1="Re-read the flavor text carefully.", hint2="Google an unusual phrase from it.", is_active=0),

    dict(slug="feed-jackolantern", title="Feed the Jack-o'-Lantern", category="Binary Exploitation",
         difficulty="medium", points=220, description="TODO: basic buffer overflow.",
         flag=h("TOH{PLACEHOLDER_10}"), hint1="How much can you stuff into the buffer?", hint2="Overwrite the return address.", is_active=0),
    dict(slug="seance-login", title="The Séance Login", category="Web Exploitation",
         difficulty="medium", points=230, description="TODO: SQL injection.",
         flag=h("TOH{PLACEHOLDER_11}"), hint1="Try breaking out of the query with a quote.", hint2="OR 1=1 is a classic for a reason.", is_active=0),
    dict(slug="ghost-in-cookies", title="Ghost in the Cookies", category="Web Exploitation",
         difficulty="medium", points=260, description="TODO: JWT alg=none.",
         flag=h("TOH{PLACEHOLDER_12}"), hint1="Decode the JWT header.", hint2="What if the algorithm were 'none'?", is_active=0),
    dict(slug="static-ouija-board", title="Static on the Ouija Board", category="Digital Forensics",
         difficulty="medium", points=240, description="TODO: pcap/FTP carving.",
         flag=h("TOH{PLACEHOLDER_13}"), hint1="Follow the TCP stream.", hint2="Look for FTP or HTTP file transfers.", is_active=0),
    dict(slug="wailing-waveform", title="The Wailing Waveform", category="Steganography",
         difficulty="medium", points=270, description="TODO: audio spectrogram stego.",
         flag=h("TOH{PLACEHOLDER_14}"), hint1="Look at the audio's spectrogram.", hint2="Some messages are meant to be seen, not heard.", is_active=0),
    dict(slug="cursed-music-box", title="The Cursed Music Box", category="Reverse Engineering",
         difficulty="medium", points=300, description="TODO: keygen-style reversing.",
         flag=h("TOH{PLACEHOLDER_15}"), hint1="Find the validation routine.", hint2="Trace what makes it print 'success'.", is_active=0),

    dict(slug="raise-the-dead", title="Raise the Dead", category="Binary Exploitation",
         difficulty="hard", points=400, description="TODO: ret2libc.",
         flag=h("TOH{PLACEHOLDER_16}"),
         hint1="What is summoned is never truly gone from the house; it merely sleeps in another room, waiting to be called by its true name.",
         hint2="Three doors lead to freedom: the door you entered by, the door already open, and the one you must build from borrowed keys.",
         is_active=0),
    dict(slug="puppet-master", title="The Puppet Master", category="Binary Exploitation",
         difficulty="hard", points=430, description="TODO: format string -> GOT overwrite.",
         flag=h("TOH{PLACEHOLDER_17}"),
         hint1="A voice that repeats everything you whisper can also be tricked into reading what it should not.",
         hint2="Somewhere a table of names points to where each spell truly lives — what if you rewrote an entry in that table?",
         is_active=0),
    dict(slug="necromancers-api", title="The Necromancer's API", category="Web Exploitation",
         difficulty="hard", points=450, description="TODO: SSRF chained to deserialization.",
         flag=h("TOH{PLACEHOLDER_18}"),
         hint1="Ask the server to fetch something on your behalf, then ask it to trust what it fetched a little too much.",
         hint2="What looks like data to you may look like instructions to something reading it from the inside.",
         is_active=0),
    dict(slug="bound-spirit", title="The Bound Spirit", category="Reverse Engineering",
         difficulty="hard", points=500, description="TODO: packed binary, anti-debug.",
         flag=h("TOH{PLACEHOLDER_19}"),
         hint1="The spirit wears a second skin it sheds only once, and only when no one it distrusts is watching.",
         hint2="What it fears is not the eye that watches, but the clock that ticks differently while being observed.",
         is_active=0),

    dict(slug="necronomicons-rsa", title="The Necronomicon's RSA", category="Cryptography",
         difficulty="insane", points=550, description="TODO: small-e / common-modulus attack.",
         flag=h("TOH{PLACEHOLDER_20}"),
         hint1="Two scrolls share the same seal but were signed with different oaths; together they say more than either alone.",
         hint2="A message raised to a small power, cast to several vessels, may be recovered whole without ever being unlocked.",
         is_active=0),
    dict(slug="awaken-kraken", title="Awaken the Kraken", category="Binary Exploitation",
         difficulty="insane", points=650, description="TODO: heap UAF, full mitigations.",
         flag=h("TOH{PLACEHOLDER_21}"),
         hint1="A room freed of its tenant still remembers its shape; the next tenant may not know it is being watched by the last.",
         hint2="What was discarded is not gone until something new claims the same grave.",
         is_active=0),
    dict(slug="final-seance", title="The Final Séance", category="Reverse Engineering",
         difficulty="insane", points=750, description="TODO: VM-obfuscated binary.",
         flag=h("TOH{PLACEHOLDER_22}"),
         hint1="This is not one spirit but a court of them, each translating the last one's words into a language of its own invention.",
         hint2="To understand the play, stop reading the script and start watching what the actors actually do, again and again.",
         is_active=0),
]


def main():
    db.init_db()
    conn = get_conn()
    active = 0
    for c in CHALLENGES:
        conn.execute(
            "INSERT OR REPLACE INTO challenges "
            "(slug, title, category, difficulty, points, description, flag_hash, hint1, hint2, is_active) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (c["slug"], c["title"], c["category"], c["difficulty"], c["points"],
             c["description"], c["flag"], c["hint1"], c["hint2"], c["is_active"]),
        )
        active += c["is_active"]
    conn.commit()
    conn.close()
    print(f"Seeded {len(CHALLENGES)} challenges ({active} active, {len(CHALLENGES)-active} draft/inactive).")


if __name__ == "__main__":
    main()
