# npm-update

Update NPM dependencies to newer patch and minor versions automatically.

> [!IMPORTANT]
> This project is *very much* a work in progress. I don't have *that* much time to work on this and such this project is not finished and code may not work the way it's intended to work.

- [npm-update](#npm-update)
  - [Dependencies](#dependencies)
  - [Install](#install)
  - [Usage](#usage)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
    - [Run tests](#run-tests)
  - [Authors and acknowledgments](#authors-and-acknowledgments)
  - [License](#license)

## Dependencies

- [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)

## Install

Clone the repository

```sh
git clone git@github.com:martendebruijn/npm-update.git
```

## Usage

Run the script inside a project with a `package.json` in the root folder:

```sh
python path/to/main.py
```

## Roadmap

- [ ] Create tests to test if minor and patch dependencies are succesfully upgraded [(#2)](https://github.com/martendebruijn/npm-update/issues/2) [(!8)](https://github.com/martendebruijn/npm-update/pull/8)
- [ ] Run project test scripts before committing anything [(#3)](https://github.com/martendebruijn/npm-update/issues/3)
- [ ] Create a merge request on GitLab (self/work hosted) [(#4)](https://github.com/martendebruijn/npm-update/issues/4)
- [ ] Create a pull request on GitHub [(#5)](https://github.com/martendebruijn/npm-update/issues/5)
- [ ] Create a merge request on GitLab [(#6)](https://github.com/martendebruijn/npm-update/issues/6)
- [ ] Add a tabel inside a details/summary in the body of a pull/merge request [(#7)](https://github.com/martendebruijn/npm-update/issues/7)

## Contributing

Clone the repository

```sh
git clone git@github.com:martendebruijn/npm-update.git
```

Install the requirements

```sh
pip install -r requirements.txt
```

### Run tests

```sh
pytest
```

## Authors and acknowledgments

- **[@martendebruijn](https://github.com/martendebruijn)** - Owner

For a full list of contributors, please see the [contributors list](https://github.com/martendebruijn/types/graphs/contributors).

## License

[MIT](./LICENSE) license

Copyright © 2024 [Marten de Bruijn](https://github.com/martendebruijn)
