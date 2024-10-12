/*
 * Chomp Food Database API Documentation
 * ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Subscription Options &raquo;](https://chompthis.com/api/)     * [Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php) 
 *
 * The version of the OpenAPI document: 1.0.0-oas3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BrandedFoodObjectItemsInnerCountryDetails;
import org.openapitools.client.model.BrandedFoodObjectItemsInnerDietFlagsInner;
import org.openapitools.client.model.BrandedFoodObjectItemsInnerDietLabels;
import org.openapitools.client.model.BrandedFoodObjectItemsInnerNutrientsInner;
import org.openapitools.client.model.BrandedFoodObjectItemsInnerPackage;
import org.openapitools.client.model.BrandedFoodObjectItemsInnerPackagingPhotos;
import org.openapitools.client.model.BrandedFoodObjectItemsInnerServing;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * An object containing information for this specific item.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:22.963103-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BrandedFoodObjectItemsInner {
  public static final String SERIALIZED_NAME_ALLERGENS = "allergens";
  @SerializedName(SERIALIZED_NAME_ALLERGENS)
  private List<String> allergens = new ArrayList<>();

  public static final String SERIALIZED_NAME_BARCODE = "barcode";
  @SerializedName(SERIALIZED_NAME_BARCODE)
  private String barcode;

  public static final String SERIALIZED_NAME_BRAND = "brand";
  @SerializedName(SERIALIZED_NAME_BRAND)
  private String brand;

  public static final String SERIALIZED_NAME_BRAND_LIST = "brand_list";
  @SerializedName(SERIALIZED_NAME_BRAND_LIST)
  private List<String> brandList = new ArrayList<>();

  public static final String SERIALIZED_NAME_CATEGORIES = "categories";
  @SerializedName(SERIALIZED_NAME_CATEGORIES)
  private List<String> categories = new ArrayList<>();

  public static final String SERIALIZED_NAME_COUNTRIES = "countries";
  @SerializedName(SERIALIZED_NAME_COUNTRIES)
  private List<String> countries = new ArrayList<>();

  public static final String SERIALIZED_NAME_COUNTRY_DETAILS = "country_details";
  @SerializedName(SERIALIZED_NAME_COUNTRY_DETAILS)
  private BrandedFoodObjectItemsInnerCountryDetails countryDetails;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DIET_FLAGS = "diet_flags";
  @SerializedName(SERIALIZED_NAME_DIET_FLAGS)
  private List<BrandedFoodObjectItemsInnerDietFlagsInner> dietFlags = new ArrayList<>();

  public static final String SERIALIZED_NAME_DIET_LABELS = "diet_labels";
  @SerializedName(SERIALIZED_NAME_DIET_LABELS)
  private BrandedFoodObjectItemsInnerDietLabels dietLabels;

  public static final String SERIALIZED_NAME_HAS_ENGLISH_INGREDIENTS = "has_english_ingredients";
  @SerializedName(SERIALIZED_NAME_HAS_ENGLISH_INGREDIENTS)
  private Boolean hasEnglishIngredients;

  public static final String SERIALIZED_NAME_INGREDIENT_LIST = "ingredient_list";
  @SerializedName(SERIALIZED_NAME_INGREDIENT_LIST)
  private List<String> ingredientList = new ArrayList<>();

  public static final String SERIALIZED_NAME_INGREDIENTS = "ingredients";
  @SerializedName(SERIALIZED_NAME_INGREDIENTS)
  private String ingredients;

  public static final String SERIALIZED_NAME_KEYWORDS = "keywords";
  @SerializedName(SERIALIZED_NAME_KEYWORDS)
  private List<String> keywords = new ArrayList<>();

  public static final String SERIALIZED_NAME_MINERALS = "minerals";
  @SerializedName(SERIALIZED_NAME_MINERALS)
  private List<String> minerals = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NUTRIENTS = "nutrients";
  @SerializedName(SERIALIZED_NAME_NUTRIENTS)
  private List<BrandedFoodObjectItemsInnerNutrientsInner> nutrients = new ArrayList<>();

  public static final String SERIALIZED_NAME_PACKAGE = "package";
  @SerializedName(SERIALIZED_NAME_PACKAGE)
  private BrandedFoodObjectItemsInnerPackage _package;

  public static final String SERIALIZED_NAME_PACKAGING_PHOTOS = "packaging_photos";
  @SerializedName(SERIALIZED_NAME_PACKAGING_PHOTOS)
  private BrandedFoodObjectItemsInnerPackagingPhotos packagingPhotos;

  public static final String SERIALIZED_NAME_PALM_OIL_INGREDIENTS = "palm_oil_ingredients";
  @SerializedName(SERIALIZED_NAME_PALM_OIL_INGREDIENTS)
  private List<String> palmOilIngredients = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVING = "serving";
  @SerializedName(SERIALIZED_NAME_SERVING)
  private BrandedFoodObjectItemsInnerServing serving;

  public static final String SERIALIZED_NAME_TRACES = "traces";
  @SerializedName(SERIALIZED_NAME_TRACES)
  private List<String> traces = new ArrayList<>();

  public static final String SERIALIZED_NAME_VITAMINS = "vitamins";
  @SerializedName(SERIALIZED_NAME_VITAMINS)
  private List<String> vitamins = new ArrayList<>();

  public BrandedFoodObjectItemsInner() {
  }

  public BrandedFoodObjectItemsInner allergens(List<String> allergens) {
    this.allergens = allergens;
    return this;
  }

  public BrandedFoodObjectItemsInner addAllergensItem(String allergensItem) {
    if (this.allergens == null) {
      this.allergens = new ArrayList<>();
    }
    this.allergens.add(allergensItem);
    return this;
  }

  /**
   * An array of ingredients in this item that may cause allergic reactions in people
   * @return allergens
   */
  @javax.annotation.Nullable
  public List<String> getAllergens() {
    return allergens;
  }

  public void setAllergens(List<String> allergens) {
    this.allergens = allergens;
  }


  public BrandedFoodObjectItemsInner barcode(String barcode) {
    this.barcode = barcode;
    return this;
  }

  /**
   * EAN/UPC barcode
   * @return barcode
   */
  @javax.annotation.Nullable
  public String getBarcode() {
    return barcode;
  }

  public void setBarcode(String barcode) {
    this.barcode = barcode;
  }


  public BrandedFoodObjectItemsInner brand(String brand) {
    this.brand = brand;
    return this;
  }

  /**
   * The brand name that owns this item
   * @return brand
   */
  @javax.annotation.Nullable
  public String getBrand() {
    return brand;
  }

  public void setBrand(String brand) {
    this.brand = brand;
  }


  public BrandedFoodObjectItemsInner brandList(List<String> brandList) {
    this.brandList = brandList;
    return this;
  }

  public BrandedFoodObjectItemsInner addBrandListItem(String brandListItem) {
    if (this.brandList == null) {
      this.brandList = new ArrayList<>();
    }
    this.brandList.add(brandListItem);
    return this;
  }

  /**
   * An array of brands we have associated with this item. Some items are sold by more than 1 brand.
   * @return brandList
   */
  @javax.annotation.Nullable
  public List<String> getBrandList() {
    return brandList;
  }

  public void setBrandList(List<String> brandList) {
    this.brandList = brandList;
  }


  public BrandedFoodObjectItemsInner categories(List<String> categories) {
    this.categories = categories;
    return this;
  }

  public BrandedFoodObjectItemsInner addCategoriesItem(String categoriesItem) {
    if (this.categories == null) {
      this.categories = new ArrayList<>();
    }
    this.categories.add(categoriesItem);
    return this;
  }

  /**
   * Get categories
   * @return categories
   */
  @javax.annotation.Nullable
  public List<String> getCategories() {
    return categories;
  }

  public void setCategories(List<String> categories) {
    this.categories = categories;
  }


  public BrandedFoodObjectItemsInner countries(List<String> countries) {
    this.countries = countries;
    return this;
  }

  public BrandedFoodObjectItemsInner addCountriesItem(String countriesItem) {
    if (this.countries == null) {
      this.countries = new ArrayList<>();
    }
    this.countries.add(countriesItem);
    return this;
  }

  /**
   * An array of countries where this item is sold
   * @return countries
   */
  @javax.annotation.Nullable
  public List<String> getCountries() {
    return countries;
  }

  public void setCountries(List<String> countries) {
    this.countries = countries;
  }


  public BrandedFoodObjectItemsInner countryDetails(BrandedFoodObjectItemsInnerCountryDetails countryDetails) {
    this.countryDetails = countryDetails;
    return this;
  }

  /**
   * Get countryDetails
   * @return countryDetails
   */
  @javax.annotation.Nullable
  public BrandedFoodObjectItemsInnerCountryDetails getCountryDetails() {
    return countryDetails;
  }

  public void setCountryDetails(BrandedFoodObjectItemsInnerCountryDetails countryDetails) {
    this.countryDetails = countryDetails;
  }


  public BrandedFoodObjectItemsInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A description of this item
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public BrandedFoodObjectItemsInner dietFlags(List<BrandedFoodObjectItemsInnerDietFlagsInner> dietFlags) {
    this.dietFlags = dietFlags;
    return this;
  }

  public BrandedFoodObjectItemsInner addDietFlagsItem(BrandedFoodObjectItemsInnerDietFlagsInner dietFlagsItem) {
    if (this.dietFlags == null) {
      this.dietFlags = new ArrayList<>();
    }
    this.dietFlags.add(dietFlagsItem);
    return this;
  }

  /**
   * An array of ingredient objects that were flagged while grading this item for compatibility with each diet
   * @return dietFlags
   */
  @javax.annotation.Nullable
  public List<BrandedFoodObjectItemsInnerDietFlagsInner> getDietFlags() {
    return dietFlags;
  }

  public void setDietFlags(List<BrandedFoodObjectItemsInnerDietFlagsInner> dietFlags) {
    this.dietFlags = dietFlags;
  }


  public BrandedFoodObjectItemsInner dietLabels(BrandedFoodObjectItemsInnerDietLabels dietLabels) {
    this.dietLabels = dietLabels;
    return this;
  }

  /**
   * Get dietLabels
   * @return dietLabels
   */
  @javax.annotation.Nullable
  public BrandedFoodObjectItemsInnerDietLabels getDietLabels() {
    return dietLabels;
  }

  public void setDietLabels(BrandedFoodObjectItemsInnerDietLabels dietLabels) {
    this.dietLabels = dietLabels;
  }


  public BrandedFoodObjectItemsInner hasEnglishIngredients(Boolean hasEnglishIngredients) {
    this.hasEnglishIngredients = hasEnglishIngredients;
    return this;
  }

  /**
   * A boolean indicating if we have English ingredients for this item
   * @return hasEnglishIngredients
   */
  @javax.annotation.Nullable
  public Boolean getHasEnglishIngredients() {
    return hasEnglishIngredients;
  }

  public void setHasEnglishIngredients(Boolean hasEnglishIngredients) {
    this.hasEnglishIngredients = hasEnglishIngredients;
  }


  public BrandedFoodObjectItemsInner ingredientList(List<String> ingredientList) {
    this.ingredientList = ingredientList;
    return this;
  }

  public BrandedFoodObjectItemsInner addIngredientListItem(String ingredientListItem) {
    if (this.ingredientList == null) {
      this.ingredientList = new ArrayList<>();
    }
    this.ingredientList.add(ingredientListItem);
    return this;
  }

  /**
   * An array of this item&#39;s ingredients
   * @return ingredientList
   */
  @javax.annotation.Nullable
  public List<String> getIngredientList() {
    return ingredientList;
  }

  public void setIngredientList(List<String> ingredientList) {
    this.ingredientList = ingredientList;
  }


  public BrandedFoodObjectItemsInner ingredients(String ingredients) {
    this.ingredients = ingredients;
    return this;
  }

  /**
   * This food item&#39;s ingredients from greatest quantity to least
   * @return ingredients
   */
  @javax.annotation.Nullable
  public String getIngredients() {
    return ingredients;
  }

  public void setIngredients(String ingredients) {
    this.ingredients = ingredients;
  }


  public BrandedFoodObjectItemsInner keywords(List<String> keywords) {
    this.keywords = keywords;
    return this;
  }

  public BrandedFoodObjectItemsInner addKeywordsItem(String keywordsItem) {
    if (this.keywords == null) {
      this.keywords = new ArrayList<>();
    }
    this.keywords.add(keywordsItem);
    return this;
  }

  /**
   * An array of keywords that can be used to describe this item
   * @return keywords
   */
  @javax.annotation.Nullable
  public List<String> getKeywords() {
    return keywords;
  }

  public void setKeywords(List<String> keywords) {
    this.keywords = keywords;
  }


  public BrandedFoodObjectItemsInner minerals(List<String> minerals) {
    this.minerals = minerals;
    return this;
  }

  public BrandedFoodObjectItemsInner addMineralsItem(String mineralsItem) {
    if (this.minerals == null) {
      this.minerals = new ArrayList<>();
    }
    this.minerals.add(mineralsItem);
    return this;
  }

  /**
   * An array of minerals that this item contains
   * @return minerals
   */
  @javax.annotation.Nullable
  public List<String> getMinerals() {
    return minerals;
  }

  public void setMinerals(List<String> minerals) {
    this.minerals = minerals;
  }


  public BrandedFoodObjectItemsInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Item name as provided by brand owner or as shown on packaging
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public BrandedFoodObjectItemsInner nutrients(List<BrandedFoodObjectItemsInnerNutrientsInner> nutrients) {
    this.nutrients = nutrients;
    return this;
  }

  public BrandedFoodObjectItemsInner addNutrientsItem(BrandedFoodObjectItemsInnerNutrientsInner nutrientsItem) {
    if (this.nutrients == null) {
      this.nutrients = new ArrayList<>();
    }
    this.nutrients.add(nutrientsItem);
    return this;
  }

  /**
   * An array containing nutrient informatio objects for this food item
   * @return nutrients
   */
  @javax.annotation.Nullable
  public List<BrandedFoodObjectItemsInnerNutrientsInner> getNutrients() {
    return nutrients;
  }

  public void setNutrients(List<BrandedFoodObjectItemsInnerNutrientsInner> nutrients) {
    this.nutrients = nutrients;
  }


  public BrandedFoodObjectItemsInner _package(BrandedFoodObjectItemsInnerPackage _package) {
    this._package = _package;
    return this;
  }

  /**
   * Get _package
   * @return _package
   */
  @javax.annotation.Nullable
  public BrandedFoodObjectItemsInnerPackage getPackage() {
    return _package;
  }

  public void setPackage(BrandedFoodObjectItemsInnerPackage _package) {
    this._package = _package;
  }


  public BrandedFoodObjectItemsInner packagingPhotos(BrandedFoodObjectItemsInnerPackagingPhotos packagingPhotos) {
    this.packagingPhotos = packagingPhotos;
    return this;
  }

  /**
   * Get packagingPhotos
   * @return packagingPhotos
   */
  @javax.annotation.Nullable
  public BrandedFoodObjectItemsInnerPackagingPhotos getPackagingPhotos() {
    return packagingPhotos;
  }

  public void setPackagingPhotos(BrandedFoodObjectItemsInnerPackagingPhotos packagingPhotos) {
    this.packagingPhotos = packagingPhotos;
  }


  public BrandedFoodObjectItemsInner palmOilIngredients(List<String> palmOilIngredients) {
    this.palmOilIngredients = palmOilIngredients;
    return this;
  }

  public BrandedFoodObjectItemsInner addPalmOilIngredientsItem(String palmOilIngredientsItem) {
    if (this.palmOilIngredients == null) {
      this.palmOilIngredients = new ArrayList<>();
    }
    this.palmOilIngredients.add(palmOilIngredientsItem);
    return this;
  }

  /**
   * An array of ingredients made from palm oil
   * @return palmOilIngredients
   */
  @javax.annotation.Nullable
  public List<String> getPalmOilIngredients() {
    return palmOilIngredients;
  }

  public void setPalmOilIngredients(List<String> palmOilIngredients) {
    this.palmOilIngredients = palmOilIngredients;
  }


  public BrandedFoodObjectItemsInner serving(BrandedFoodObjectItemsInnerServing serving) {
    this.serving = serving;
    return this;
  }

  /**
   * Get serving
   * @return serving
   */
  @javax.annotation.Nullable
  public BrandedFoodObjectItemsInnerServing getServing() {
    return serving;
  }

  public void setServing(BrandedFoodObjectItemsInnerServing serving) {
    this.serving = serving;
  }


  public BrandedFoodObjectItemsInner traces(List<String> traces) {
    this.traces = traces;
    return this;
  }

  public BrandedFoodObjectItemsInner addTracesItem(String tracesItem) {
    if (this.traces == null) {
      this.traces = new ArrayList<>();
    }
    this.traces.add(tracesItem);
    return this;
  }

  /**
   * An array of trace ingredients that may be found in this item
   * @return traces
   */
  @javax.annotation.Nullable
  public List<String> getTraces() {
    return traces;
  }

  public void setTraces(List<String> traces) {
    this.traces = traces;
  }


  public BrandedFoodObjectItemsInner vitamins(List<String> vitamins) {
    this.vitamins = vitamins;
    return this;
  }

  public BrandedFoodObjectItemsInner addVitaminsItem(String vitaminsItem) {
    if (this.vitamins == null) {
      this.vitamins = new ArrayList<>();
    }
    this.vitamins.add(vitaminsItem);
    return this;
  }

  /**
   * An array of vitamins that are found in this item
   * @return vitamins
   */
  @javax.annotation.Nullable
  public List<String> getVitamins() {
    return vitamins;
  }

  public void setVitamins(List<String> vitamins) {
    this.vitamins = vitamins;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BrandedFoodObjectItemsInner brandedFoodObjectItemsInner = (BrandedFoodObjectItemsInner) o;
    return Objects.equals(this.allergens, brandedFoodObjectItemsInner.allergens) &&
        Objects.equals(this.barcode, brandedFoodObjectItemsInner.barcode) &&
        Objects.equals(this.brand, brandedFoodObjectItemsInner.brand) &&
        Objects.equals(this.brandList, brandedFoodObjectItemsInner.brandList) &&
        Objects.equals(this.categories, brandedFoodObjectItemsInner.categories) &&
        Objects.equals(this.countries, brandedFoodObjectItemsInner.countries) &&
        Objects.equals(this.countryDetails, brandedFoodObjectItemsInner.countryDetails) &&
        Objects.equals(this.description, brandedFoodObjectItemsInner.description) &&
        Objects.equals(this.dietFlags, brandedFoodObjectItemsInner.dietFlags) &&
        Objects.equals(this.dietLabels, brandedFoodObjectItemsInner.dietLabels) &&
        Objects.equals(this.hasEnglishIngredients, brandedFoodObjectItemsInner.hasEnglishIngredients) &&
        Objects.equals(this.ingredientList, brandedFoodObjectItemsInner.ingredientList) &&
        Objects.equals(this.ingredients, brandedFoodObjectItemsInner.ingredients) &&
        Objects.equals(this.keywords, brandedFoodObjectItemsInner.keywords) &&
        Objects.equals(this.minerals, brandedFoodObjectItemsInner.minerals) &&
        Objects.equals(this.name, brandedFoodObjectItemsInner.name) &&
        Objects.equals(this.nutrients, brandedFoodObjectItemsInner.nutrients) &&
        Objects.equals(this._package, brandedFoodObjectItemsInner._package) &&
        Objects.equals(this.packagingPhotos, brandedFoodObjectItemsInner.packagingPhotos) &&
        Objects.equals(this.palmOilIngredients, brandedFoodObjectItemsInner.palmOilIngredients) &&
        Objects.equals(this.serving, brandedFoodObjectItemsInner.serving) &&
        Objects.equals(this.traces, brandedFoodObjectItemsInner.traces) &&
        Objects.equals(this.vitamins, brandedFoodObjectItemsInner.vitamins);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allergens, barcode, brand, brandList, categories, countries, countryDetails, description, dietFlags, dietLabels, hasEnglishIngredients, ingredientList, ingredients, keywords, minerals, name, nutrients, _package, packagingPhotos, palmOilIngredients, serving, traces, vitamins);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BrandedFoodObjectItemsInner {\n");
    sb.append("    allergens: ").append(toIndentedString(allergens)).append("\n");
    sb.append("    barcode: ").append(toIndentedString(barcode)).append("\n");
    sb.append("    brand: ").append(toIndentedString(brand)).append("\n");
    sb.append("    brandList: ").append(toIndentedString(brandList)).append("\n");
    sb.append("    categories: ").append(toIndentedString(categories)).append("\n");
    sb.append("    countries: ").append(toIndentedString(countries)).append("\n");
    sb.append("    countryDetails: ").append(toIndentedString(countryDetails)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    dietFlags: ").append(toIndentedString(dietFlags)).append("\n");
    sb.append("    dietLabels: ").append(toIndentedString(dietLabels)).append("\n");
    sb.append("    hasEnglishIngredients: ").append(toIndentedString(hasEnglishIngredients)).append("\n");
    sb.append("    ingredientList: ").append(toIndentedString(ingredientList)).append("\n");
    sb.append("    ingredients: ").append(toIndentedString(ingredients)).append("\n");
    sb.append("    keywords: ").append(toIndentedString(keywords)).append("\n");
    sb.append("    minerals: ").append(toIndentedString(minerals)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nutrients: ").append(toIndentedString(nutrients)).append("\n");
    sb.append("    _package: ").append(toIndentedString(_package)).append("\n");
    sb.append("    packagingPhotos: ").append(toIndentedString(packagingPhotos)).append("\n");
    sb.append("    palmOilIngredients: ").append(toIndentedString(palmOilIngredients)).append("\n");
    sb.append("    serving: ").append(toIndentedString(serving)).append("\n");
    sb.append("    traces: ").append(toIndentedString(traces)).append("\n");
    sb.append("    vitamins: ").append(toIndentedString(vitamins)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("allergens");
    openapiFields.add("barcode");
    openapiFields.add("brand");
    openapiFields.add("brand_list");
    openapiFields.add("categories");
    openapiFields.add("countries");
    openapiFields.add("country_details");
    openapiFields.add("description");
    openapiFields.add("diet_flags");
    openapiFields.add("diet_labels");
    openapiFields.add("has_english_ingredients");
    openapiFields.add("ingredient_list");
    openapiFields.add("ingredients");
    openapiFields.add("keywords");
    openapiFields.add("minerals");
    openapiFields.add("name");
    openapiFields.add("nutrients");
    openapiFields.add("package");
    openapiFields.add("packaging_photos");
    openapiFields.add("palm_oil_ingredients");
    openapiFields.add("serving");
    openapiFields.add("traces");
    openapiFields.add("vitamins");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BrandedFoodObjectItemsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BrandedFoodObjectItemsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BrandedFoodObjectItemsInner is not found in the empty JSON string", BrandedFoodObjectItemsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BrandedFoodObjectItemsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BrandedFoodObjectItemsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("allergens") != null && !jsonObj.get("allergens").isJsonNull() && !jsonObj.get("allergens").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `allergens` to be an array in the JSON string but got `%s`", jsonObj.get("allergens").toString()));
      }
      if ((jsonObj.get("barcode") != null && !jsonObj.get("barcode").isJsonNull()) && !jsonObj.get("barcode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `barcode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("barcode").toString()));
      }
      if ((jsonObj.get("brand") != null && !jsonObj.get("brand").isJsonNull()) && !jsonObj.get("brand").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `brand` to be a primitive type in the JSON string but got `%s`", jsonObj.get("brand").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("brand_list") != null && !jsonObj.get("brand_list").isJsonNull() && !jsonObj.get("brand_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `brand_list` to be an array in the JSON string but got `%s`", jsonObj.get("brand_list").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("categories") != null && !jsonObj.get("categories").isJsonNull() && !jsonObj.get("categories").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `categories` to be an array in the JSON string but got `%s`", jsonObj.get("categories").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("countries") != null && !jsonObj.get("countries").isJsonNull() && !jsonObj.get("countries").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `countries` to be an array in the JSON string but got `%s`", jsonObj.get("countries").toString()));
      }
      // validate the optional field `country_details`
      if (jsonObj.get("country_details") != null && !jsonObj.get("country_details").isJsonNull()) {
        BrandedFoodObjectItemsInnerCountryDetails.validateJsonElement(jsonObj.get("country_details"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("diet_flags") != null && !jsonObj.get("diet_flags").isJsonNull()) {
        JsonArray jsonArraydietFlags = jsonObj.getAsJsonArray("diet_flags");
        if (jsonArraydietFlags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("diet_flags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `diet_flags` to be an array in the JSON string but got `%s`", jsonObj.get("diet_flags").toString()));
          }

          // validate the optional field `diet_flags` (array)
          for (int i = 0; i < jsonArraydietFlags.size(); i++) {
            BrandedFoodObjectItemsInnerDietFlagsInner.validateJsonElement(jsonArraydietFlags.get(i));
          };
        }
      }
      // validate the optional field `diet_labels`
      if (jsonObj.get("diet_labels") != null && !jsonObj.get("diet_labels").isJsonNull()) {
        BrandedFoodObjectItemsInnerDietLabels.validateJsonElement(jsonObj.get("diet_labels"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("ingredient_list") != null && !jsonObj.get("ingredient_list").isJsonNull() && !jsonObj.get("ingredient_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ingredient_list` to be an array in the JSON string but got `%s`", jsonObj.get("ingredient_list").toString()));
      }
      if ((jsonObj.get("ingredients") != null && !jsonObj.get("ingredients").isJsonNull()) && !jsonObj.get("ingredients").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ingredients` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ingredients").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("keywords") != null && !jsonObj.get("keywords").isJsonNull() && !jsonObj.get("keywords").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `keywords` to be an array in the JSON string but got `%s`", jsonObj.get("keywords").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("minerals") != null && !jsonObj.get("minerals").isJsonNull() && !jsonObj.get("minerals").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `minerals` to be an array in the JSON string but got `%s`", jsonObj.get("minerals").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("nutrients") != null && !jsonObj.get("nutrients").isJsonNull()) {
        JsonArray jsonArraynutrients = jsonObj.getAsJsonArray("nutrients");
        if (jsonArraynutrients != null) {
          // ensure the json data is an array
          if (!jsonObj.get("nutrients").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `nutrients` to be an array in the JSON string but got `%s`", jsonObj.get("nutrients").toString()));
          }

          // validate the optional field `nutrients` (array)
          for (int i = 0; i < jsonArraynutrients.size(); i++) {
            BrandedFoodObjectItemsInnerNutrientsInner.validateJsonElement(jsonArraynutrients.get(i));
          };
        }
      }
      // validate the optional field `package`
      if (jsonObj.get("package") != null && !jsonObj.get("package").isJsonNull()) {
        BrandedFoodObjectItemsInnerPackage.validateJsonElement(jsonObj.get("package"));
      }
      // validate the optional field `packaging_photos`
      if (jsonObj.get("packaging_photos") != null && !jsonObj.get("packaging_photos").isJsonNull()) {
        BrandedFoodObjectItemsInnerPackagingPhotos.validateJsonElement(jsonObj.get("packaging_photos"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("palm_oil_ingredients") != null && !jsonObj.get("palm_oil_ingredients").isJsonNull() && !jsonObj.get("palm_oil_ingredients").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `palm_oil_ingredients` to be an array in the JSON string but got `%s`", jsonObj.get("palm_oil_ingredients").toString()));
      }
      // validate the optional field `serving`
      if (jsonObj.get("serving") != null && !jsonObj.get("serving").isJsonNull()) {
        BrandedFoodObjectItemsInnerServing.validateJsonElement(jsonObj.get("serving"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("traces") != null && !jsonObj.get("traces").isJsonNull() && !jsonObj.get("traces").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `traces` to be an array in the JSON string but got `%s`", jsonObj.get("traces").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("vitamins") != null && !jsonObj.get("vitamins").isJsonNull() && !jsonObj.get("vitamins").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `vitamins` to be an array in the JSON string but got `%s`", jsonObj.get("vitamins").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BrandedFoodObjectItemsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BrandedFoodObjectItemsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BrandedFoodObjectItemsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BrandedFoodObjectItemsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<BrandedFoodObjectItemsInner>() {
           @Override
           public void write(JsonWriter out, BrandedFoodObjectItemsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BrandedFoodObjectItemsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BrandedFoodObjectItemsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BrandedFoodObjectItemsInner
   * @throws IOException if the JSON string is invalid with respect to BrandedFoodObjectItemsInner
   */
  public static BrandedFoodObjectItemsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BrandedFoodObjectItemsInner.class);
  }

  /**
   * Convert an instance of BrandedFoodObjectItemsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

