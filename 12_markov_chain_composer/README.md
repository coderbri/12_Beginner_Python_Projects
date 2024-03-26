# 12 Markov Chain Composer

I finished a project called Markov Chain Composer based on Kylie Ying's tutorial on Beginner Python Projects. The code I made is below:
```py
```

The lyrics.py file is a scraper using lyricsgenius:
```py
```

Please help generate for me a GitHub README
- explaining what is a Markov Chain
<!-- - how this is used to represent AI -->
- what is a graph composer and what are nodes
- explain the logic in graph.py
- explain the logic in compose.py



## Overview
<!-- <div align="center">
    <img src="" alt="alt" width="450px" height="auto">
</div> -->





Certainly! Here's an updated README with the breakdown and a table of contents:

---

# Markov Chain Text Composer

## Table of Contents
- [Overview](#overview)
- [What is a Markov Chain?](#what-is-a-markov-chain)
- [What is a Graph Composer and Nodes?](#what-is-a-graph-composer-and-nodes)
- [Application in Text Composition](#application-in-text-composition)
   - [Logic in lyrics.py](#logic-in-lyricspy)
   - [Logic in graph.py](#logic-in-grapypy)
   - [Logic in compose.py](#logic-in-composepy)
- [Getting Started](#getting-started)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [Credits](#credits)

## Overview

This project implements a **Markov Chain Text Composer**, a type of algorithm that generates new text based on the statistical properties of a given input text. It utilizes concepts from graph theory and probability to create compositions that mimic the style and structure of the original text.

## What is a Markov Chain?

A Markov Chain is a stochastic model that describes a sequence of events where the probability of each event depends only on the state attained in the previous event. In simpler terms, it's a process that transitions between different states, with each transition governed by probabilities determined by the current state.

## What is a Graph Composer and Nodes?

A Graph Composer is a program that constructs and manipulates graphs, which are mathematical structures representing relationships between entities. In the context of this project, nodes refer to the individual elements within the graph, each representing a distinct entity or state.

## Application in Text Composition

### Logic in lyrics.py

#### `save_lyrics(songs, artist_name, album_name)`
- **Purpose**: Saves the lyrics of specified songs by a given artist into text files.
- **Connection to Logic**: 
  - Iterates through the list of song titles (`songs`).
  - Searches for each song using the Genius API (`genius.search_song(song_title, artist_name)`).
  - Retrieves the lyrics for each song and saves them into text files named based on artist and album.
  - Handles any potential errors, such as invalid song titles or network issues.

### Logic in graph.py

#### `Vertex` class
- **Purpose**: Represents a node in the graph, each corresponding to a word in the input text.
- **Connection to Logic**:
  - Stores the value of the word (`value`) and a dictionary of adjacent vertices (`adjacent`).
  - Provides methods to add edges to other vertices, increment edge weights, get adjacent nodes, and generate probability mappings.

#### `Graph` class
- **Purpose**: Represents the entire graph structure composed of vertices and their relationships.
- **Connection to Logic**:
  - Contains a dictionary of vertices (`vertices`).
  - Provides methods to add vertices, get vertices, get vertex values, get the next word for a given vertex, and generate probability mappings for all vertices.

### Logic in compose.py

#### `get_words_from_text(text_path)`
- **Purpose**: Extracts words from the input text file.
- **Connection to Logic**:
  - Reads the text file and removes unnecessary characters (e.g., punctuation, special characters).
  - Converts the text to lowercase for uniformity.
  - Splits the text into individual words and returns a list of words.

#### `make_graph(words)`
- **Purpose**: Constructs a graph representation based on the input words.
- **Connection to Logic**:
  - Iterates through the list of words and creates vertices for each unique word.
  - Establishes relationships between adjacent words by adding edges between corresponding vertices.
  - Calculates probabilities for transitioning between words based on edge weights.

#### `compose(g, words, length=50)`
- **Purpose**: Generates a new composition using the Markov Chain model.
- **Connection to Logic**:
  - Selects a random starting word from the input words.
  - Iterates through the graph, selecting subsequent words probabilistically based on edge weights.
  - Constructs a composition of specified length by chaining together the selected words.

#### `main()`
- **Purpose**: Entry point of the composition process.
- **Connection to Logic**:
  - Retrieves words from text sources using `get_words_from_text`.
  - Constructs a graph representation using `make_graph`.
  - Generates a new composition using `compose`.
  - Prints the composed text for user interaction.

## Getting Started

To use the Markov Chain Text Composer:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Follow the instructions in the `compose.py` file to compose text from song lyrics or other text sources.

## Example Usage

```bash
python3 compose.py
```

This command will execute the composition process and generate a new text composition based on the provided input data.

## Credits

This project is based on the Python Image Manipulation tutorial by Kylie Ying.

### Notes by Creator

Using Markov Chain to represent relationships between words in song lyrics and then generating new lyrics... ahem interpretive poetry... from the graph

You'll have to slightly change some of the code in order to adjust length of composition/which file is the vocabulary for the composition.


---
<p align="right">Completed: ２０２４年０３月２１日（木）</p>
