# Document Word Summarizer

Coding exercise to read a series of text files and produce a summary of the words found.  
  
This includes: 
- the word
- number of occurrences
- documents in which the word appeared
- sentences in which the word appeared  

## Set up your virtualenv with Python 3.7

Assuming virtualenv is already installed on your system.  
If using a virtualenvwrapper then set up a virtual environment for this project 
eg.
```
mkvirtualenv -p /usr/bin/python3.7 -a [path to project] [virtualenv name]
```
Otherwise set up your virtual environment as you normally would.  

Once your virtualenv is active, from the project root dir install the necessary dependencies

```
pip3 install -r requirements.txt
```

## Run unittests
From the project root ...
```bash 
pytest -v test_document_word_counter.py
```


## Run script
Designed to run for an arbitrary list of words deemed to be of interest, rather than report on every single word found.
```bash
python document_word_counter.py
```

## Example output
```bash
┌─────────────────┬───────┬────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│      Word       │ Count │ Documents  │ Sentences containing the word                                                                                         │
├─────────────────┼───────┼────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│     Russia      │   6   │  doc6.txt  │ As some of you know, Senator Lugar and I recently traveled to Russia, Ukraine, and Azerbaijan to witness firsthand bo │
│                 │       │            │ th the progress we're making in securing the world's most dangerous weapons, as well as the serious challenges that l │
│                 │       │            │ ie ahead |                                                                                                            │
│                 │       │            │ And so the question we need to be asking ourselves today is, what is the future of this program? With the situation i │
│                 │       │            │ n Russia and the rest of the former Soviet Union so drastically different than it was in 1991, or even in 1996 or 200 │
│                 │       │            │ 1, what must we do to effectively confront this threat in the days and years to come? |                               │
│                 │       │            │ First, the Nunn-Lugar program should be more engaged in containing proliferation threats from Soviet-supplied, civili │
│                 │       │            │ an research reactors throughout Russia and the Independent States |                                                   │
│                 │       │            │ In the years ahead, this should become an increasing priority for the Nunn-Lugar program, the Congress, and the Russi │
│                 │       │            │ ans, who are already taking important steps to help implement these programs |                                        │
│                 │       │            │ One of the most important steps is for Russia to permit the access and transparency necessary to deal with the threat │
│                 │       │            │  |                                                                                                                    │
│                 │       │            │ As the Avian Influenza outbreak demonstrates, even the zealous Russian border guard is helpless against the global sw │
│                 │       │            │ eep of biological threats |                                                                                           │
│                 │       │            │ Additionally, in the last few years, we've seen some disturbing trends from Russia itself - the deterioration of demo │
│                 │       │            │ cracy and the rule of law, the abuses that have taken place in Chechnya, Russian meddling in the former Soviet Union  │
│                 │       │            │ - that raise serious questions about our relationship |                                                               │
│                 │       │            │ -Russian relationship to deteriorate to the point where Russia does not think it's in their best interest to help us  │
│                 │       │            │ finish the job we started |                                                                                           │
│                 │       │            │ One way we could strengthen this relationship is by thinking about the Russians as more of a partner and less of a su │
│                 │       │            │ bordinate in the Cooperative Threat Reduction effort |                                                                │
│                 │       │            │ Time and time again on the trip, I saw their skill and experience when negotiating with the Russians |                │
│                 │       │            │ But thinking of the Russians more as partners does mean being more thoughtful, respectful, and consistent about what  │
│                 │       │            │ we say and what we do |                                                                                               │
│                 │       │            │ It means that the Russians can and should do more to support these programs                                           │
├─────────────────┼───────┼────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤

```