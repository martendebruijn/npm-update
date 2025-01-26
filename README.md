# npm-update

Update NPM dependencies to newer patch and minor versions automatically.

> [!IMPORTANT]
> This project is *very much* a work in progress. I don't have *that* much time to work on this and such this project is not finished and code may not work the way it's intended to work.

- [npm-update](#npm-update)
  - [Dependencies](#dependencies)
  - [Install](#install)
  - [Usage](#usage)
  - [Roadmap](#roadmap)
  - [Authors and acknowledgments](#authors-and-acknowledgments)
  - [License](#license)

## Dependencies

- [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)

## Install

```sh
git clone git@github.com:martendebruijn/npm-update.git
```

## Usage

Run the script inside a project with a `package.json` in the root folder:

```sh
python path/to/main.py
```

## Roadmap

- [ ] Create tests to test if minor and patch dependencies are succesfully upgraded
- [ ] Run project test scripts before committing anything
- [ ] Create a merge request on GitLab (self/work hosted)
- [ ] Create a pull request on GitHub
- [ ] Create a merge request on GitLab
- [ ] Add a tabel inside a details/summary in the body of a pull/merge request

## Authors and acknowledgments

- **[@martendebruijn](https://github.com/martendebruijn)** - Owner

For a full list of contributors, please see the [contributors list](https://github.com/martendebruijn/types/graphs/contributors).

## License

[MIT](./LICENSE) license

Copyright © 2024 [Marten de Bruijn](https://github.com/martendebruijn)
