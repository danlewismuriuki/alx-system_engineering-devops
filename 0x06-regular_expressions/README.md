# Regular Expressions (Regex) Cheat Sheet

Regular expressions (regex or regexp) are patterns used to match character combinations in strings. They can be used in various programming languages and text editors for tasks such as search, validation, and text manipulation.

## Basics

- `.`: Matches any single character except newline.
- `*`: Matches zero or more occurrences of the preceding character or group.
- `+`: Matches one or more occurrences of the preceding character or group.
- `?`: Matches zero or one occurrence of the preceding character or group.
- `\`: Escapes a metacharacter, allowing it to be used as a literal character.

## Character Classes

- `[abc]`: Matches any single character within the brackets.
- `[^abc]`: Matches any single character not within the brackets.
- `\d`: Matches any digit (equivalent to `[0-9]`).
- `\w`: Matches any word character (alphanumeric and underscore).
- `\s`: Matches any whitespace character (space, tab, newline).

## Anchors

- `^`: Matches the beginning of a line.
- `$`: Matches the end of a line.

## Groups and Capturing

- `()`: Groups multiple tokens together.
- `(?:)`: Groups without capturing.
- `(?<name>)`: Capturing group with a specified name.

## Quantifiers

- `{n}`: Matches exactly n occurrences of the preceding character or group.
- `{n,}`: Matches n or more occurrences of the preceding character or group.
- `{n,m}`: Matches between n and m occurrences of the preceding character or group.

## Examples

- `\d{3}`: Matches any three digits.
- `\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b`: Matches an email address.

## Tools

- [Regex101](https://regex101.com/): Online regex tester and debugger.
- [Regexr](https://regexr.com/): Another online regex tester with a focus on JavaScript.

For more detailed information and examples, refer to the documentation of your programming language or text editor.

