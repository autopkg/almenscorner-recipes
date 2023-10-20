almenscorner-recipes
=======

A set of recipes for use with the [IntuneAppUploader](https://github.com/almenscorner/intune-uploader) processor.

To use the recipes, add this repository to your autopkg repos and create overrides:

```bash
autopkg repo-add almenscorner-recipes
```

```bash
autopkg make-override Spotify.intune.recipe
```

## Dependencies
Most of the recipes in this repository have a dependency on a parent recipe for downloading the application. To find which recipe repos you need to add to use a specific recipe, look up the `ParentRecipe` key in the recipe. This gives you an idea of which recipe repos you need to add to your autopkg installation. Also, keep in mind that some recipes have dependencies on other recipes, so you might need to add more than one recipe repo.
