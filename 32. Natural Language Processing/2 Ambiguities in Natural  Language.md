# Ambiguities in Natural Language Processing

Ambiguity is a core challenge in NLP - the same words can mean completely different things depending on context. Every complex sentence can have multiple interpretations, making accurate language understanding difficult.

## Types of Ambiguity

### 1. Lexical Ambiguity
One word, multiple meanings based on context.

**5 Easy Examples:**
- "BANK": Riverbank vs. Money bank
- "BAT": Flying animal vs. Baseball bat  
- "LIGHT": Not heavy vs. Brightness
- "MATCH": Fire starter vs. Sports game
- "CRANE": Bird vs. Construction machine

**Key:** Same word = different dictionary meanings.

### 2. Syntactic Ambiguity
Sentence structure allows multiple parsings.

**5 Easy Examples:**
- "I saw her duck." (She avoided OR pet bird?)
- "The chicken is ready to eat." (Hungry chicken OR dinner?)
- "Visiting relatives can be boring." (Boring relatives OR boring activity?)
- "He fed her cat food." (Cat's food OR food for her?)
- "Old men and women." (Men only old OR both old?)

**Key:** Grammar allows 2+ valid sentence structures.

### 3. Semantic Ambiguity
Clear syntax, unclear word relationships/meanings.

**5 Easy Examples:**
- "The duck is ready to eat." (Eat duck OR duck eating?)
- "Time flies like an arrow." (Time moves fast OR measure time?)
- "I made her duck." (Forced her OR cooked pet?)
- "They are cooking apples." (Making apple dish OR angry apples?)
- "The man returned to his house annoyed." (House owner annoyed OR returned annoyed?)

**Key:** Logical connections unclear.

### 4. Anaphoric Ambiguity
Pronouns with multiple possible referents.

**5 Easy Examples:**
- "John hit Bill, then he cried." (John or Bill cried?)
- "Lisa told Sarah she failed." (Lisa or Sarah failed?)
- "Mike warned Tom he was late." (Mike or Tom late?)
- "The teacher praised the student who studied." (Teacher or student studied?)
- "Peter called Andrew stupid, then he left." (Peter or Andrew left?)

**Key:** Pronoun could refer to multiple nouns.

### 5. Pragmatic Ambiguity
Unclear speaker intent/context/understanding.

**5 Easy Examples:**
- "Can you pass the salt?" (Request OR ability question?)
- "Nice weather!" (During rain = sarcasm)
- "Break a leg!" (Good luck OR literal injury?)
- "I'm fine." (Actually upset)
- "Watch your head!" (Danger OR hairstyle comment?)

**Key:** Real intent differs from literal meaning.

## Other NLP Challenges

### 1. Homophones (Sound-Alike Words)
Words that sound identical but mean different things.

**Examples:**
- "RECKOGNIZE SPEECH" → "WRECK A NICE SPEECH"
- "YOUTH IN ASIA" → "EUTHANASIA"  
- "PAIR OF PEARS" → "PARROT PEARS"
- "KNIGHT TIME" → "NIGHT TIME"
- "SEA SICK" → "SEE SICK"

**Problem:** Speech recognition gets confused.

### 2. Context Retention
Computers struggle to track conversation context.

**Examples:**
- User: "What's the weather?"
- AI: "Sunny in NYC"
- User: "And temperature?"
- AI: "25°C" (Forgets NYC context!)


**Problem:** Loses thread of ongoing conversation.

---

## Why This Matters for NLP
- Chatbots give wrong answers
- Search engines miss results
- Voice assistants misunderstand speech
- Translation creates confusion

**Solution:** Context awareness + world knowledge needed.
