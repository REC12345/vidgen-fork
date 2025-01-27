import re

def replace_words(text: str, replacement_dict: dict) -> str:
    """
    Replaces words in the given text based on the provided replacement dictionary.

    Args:
        text: The input text to be processed.
        replacement_dict: Words to be replaced and their replacements.

    Returns:
        The text with the specified words replaced.

    """
    for k, v in replacement_dict.items():
        text = text.lower().replace(k.lower(), v)
    return text

def split_text_into_chunks(text: str, max_chunk_length: int = 300) -> list:
    """
    Split a given text into chunks of a maximum character count.

    Args:
        text: The text to be split into chunks.
        max_chunk_length: The maximum character count for each chunk.

    Returns:
        A list of chunks, where each chunk is a string.
    """
    
    sentence_pattern = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")
    sentence_boundaries = sentence_pattern.split(text)

    chunks = []
    current_chunk = ""

    for sentence in sentence_boundaries:
        sentence = sentence.replace('.', '. ')
        
        if len(current_chunk) + len(sentence) <= max_chunk_length:
            current_chunk += ' ' + sentence
        else:
            chunks.append(current_chunk)
            current_chunk = sentence

    if current_chunk:
        # Add the last chunk
        chunks.append(current_chunk)

    return chunks

def shorten_string(input_string: str, max_length: int = 20) -> str:
    """
    Shortens a given input string to a maximum length, appending '...' if necessary.

    Args:
        input_string: The input string to be shortened.
        max_length: The maximum length of the shortened string.

    Returns:
        The shortened string.
    """
    if len(input_string) <= max_length:
        return input_string
    else:
        return input_string[:max_length-3] + '...'

def shorten_hash(sha_string: str, prefix_length: int = 6, suffix_length: int = 6) -> str:
    """
    Shortens a SHA string by truncating it and adding ellipsis in the middle.
    
    Args:
        sha_string: The SHA string to be shortened.
        prefix_length: The length of the prefix to keep. Default is 6.
        suffix_length: The length of the suffix to keep. Default is 6.
    
    Returns:
        The shortened SHA string.
    """
    if len(sha_string) <= prefix_length + suffix_length:
        return sha_string
    else:
        return f"{sha_string[:prefix_length]}...{sha_string[-suffix_length:]}"

