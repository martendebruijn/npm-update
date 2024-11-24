# npm-update

Update NPM dependencies

- [npm-update](#npm-update)
  - [Dependencies](#dependencies)
  - [Install](#install)
  - [Usage](#usage)
  - [Authors and acknowledgments](#authors-and-acknowledgments)
  - [License](#license)

## Dependencies

- Python
- NPM
- packaging

## Install

```sh
git clone git@github.com:martendebruijn/npm-update.git

python -m venv vevn
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the script inside a project with a `package.json` in the root folder:

```sh
python path/to/main.py
```

## Authors and acknowledgments

- **[@martendebruijn](https://github.com/martendebruijn)** - Owner

For a full list of contributors, please see the [contributors list](https://github.com/martendebruijn/types/graphs/contributors).

## License

[MIT](./LICENSE) license

Copyright © 2024 [Marten de Bruijn](https://github.com/martendebruijn)
