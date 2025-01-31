import json
import re
from spellchecker import SpellChecker


# ---------------------------
# ---------- .json ----------
# ---------------------------


def read_json(filepath: str) -> dict:
    """
        Returns the contents of a given JSON file.
        :parameter filepath:
    """
    with open(filepath, "r") as file:
        contents: dict = json.loads(file.read())
        file.close()
    return contents


def write_json(filepath: str, content: dict) -> None:
    """
        Writes the given content to a given JSON file.
        :parameter filepath:
        :parameter content:
    """
    with open(filepath, "w") as file:
        file.write(json.dumps(content, indent=4, separators=(", ", ": ")))
        file.close()


def create_json(filename: str) -> None:
    """
        Creates a new JSON file.
        :parameter filename:
    """
    with open(filename.__add__(".json"), "x") as file:
        file.close()


# ---------------------------
# ---------- .txt -----------
# ---------------------------


def read_txt(filepath: str) -> list[str]:
    """
        This function takes a text file and returns
        its content as a list of formatted strings.
        Each word is read from the given file(1),
        formatted(2), and then inserted into the list(3).
        :param filepath:
    """
    # 1 - read words
    with open(filepath, "r") as file:
        words: list[str] = re.split(r' +|\n+', file.read())
        file.close()
    # 2 - format each word
    spellChecker: SpellChecker = SpellChecker()
    quoteMe: tuple = (
        ('"', "'", "{", "[", "("),
        (")", "]", "}", "'", '"')
    )
    for i in range(0, len(words)):
        try:
            word: str = words[i]
        except IndexError as e:
            print("\n[*] IndexError: " + str(e) + "\n")
            break
        punctuated: bool = False
        quotes: bool = False
        # 2a - pruning
        if word == '':
            words.remove('')
            i += 1
            continue
        if word.startswith(quoteMe[0]) and word.endswith(quoteMe[1]):
            quotes = True
            word = word[1 : len(word) - 1]
        if word.endswith((".", "?", "!")):
            punctuated = True
            word = re.split(r'\.+|\?+|!', word)[0]
        # 2b - spellchecking
        if spellChecker.correction(word) is not None:
            word = spellChecker.correction(word)
        else:
            quotes = True
        if punctuated:
            word = word + "."
        if quotes:
            word = '"' + word + '"'
        # 3 - append words
        words[i]: str = word.lower()
    return words


def write_txt(filepath: str, content: str | list | tuple | dict) -> None:
    """
        Writes the given content to a given Text file.
        :parameter filepath:
        :parameter content:
    """
    content = str(content)
    with open(filepath, "w") as file:
        file.write(content)
        file.close()


def create_txt(filename: str) -> None:
    """
        Creates a new Text file.
        :parameter filename:
    """
    with open(filename.__add__(".txt"), "x") as file:
        file.close()


# ---------------------------
# ---------- .srt -----------
# ---------------------------


def read_srt(filepath: str) -> dict:
    """
        Returns the contents of a given srt file.
        The format is dict[str(timestamps), str(text)].
        The timestamp is formatted as hrs:mins:seconds,milliseconds
        :parameter filepath:
    """
    with open(filepath, "r") as file:
        rawSubtitles: list[str] = re.split(r'\n\n+', file.read())
        file.close()
    subtitles: dict[str, str]= {}
    for i in range(0, len(rawSubtitles)):
        components: list[str] = re.split(r'\n', rawSubtitles[i])
        subtitles[components[1]] = components[2]
    return subtitles


def write_srt(filepath: str, content: dict) -> None:
    """
        Writes the given content to a given srt file.
        The format is dict[str(timestamps), str(text)].
        The timestamp is formatted as hrs:mins:seconds,milliseconds
        :parameter filepath:
        :parameter content:
    """
    with open(filepath, "w") as file:
        line: int = 1
        for time in content:
            file.write(f"{line}\n{time}\n{content.get(time)}\n\n")
            line += 1
        file.close()


def create_srt(filename: str) -> None:
    """
        Creates a new srt file.
        :parameter filename:
    """
    with open(filename.__add__(".srt"), "x") as file:
        file.close()