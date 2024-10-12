# FacetsApi

All URIs are relative to *https://api.zalando.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**facetsGet**](FacetsApi.md#facetsGet) | **GET** /facets | Shop Facets |


<a id="facetsGet"></a>
# **facetsGet**
> List&lt;Facet&gt; facetsGet(ageGroup, articleId, activationDate, articleModelId, assortmentArea, brand, brandfamily, category, color, den, filling, gender, heelForm, heelHeight, length, occasion, pattern, price, sale, season, shaftHeight, shaftWidth, shirtCollar, shoeFastener, shoeToecap, shopArea, size, sports, technology, trouserRise, upperMaterial, volume, acceptLanguage, fields)

Shop Facets

Zalando API Facets Schema

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zalando.com");

    FacetsApi apiInstance = new FacetsApi(defaultClient);
    List<String> ageGroup = Arrays.asList(); // List<String> | filters by age group (eg: kids)
    List<String> articleId = Arrays.asList(); // List<String> | The `articleIds` to use use for filtering.  One or more `articleIds` might be used as a filter criteria. Submit multiple `articleId` request parameters for more than one to be used. They will be treated as `OR` criteria.
    List<String> activationDate = Arrays.asList(); // List<String> | period or time the articles are activated for selling in the shop
    List<String> articleModelId = Arrays.asList(); // List<String> | filters by article ModelId
    List<String> assortmentArea = Arrays.asList(); // List<String> | filters by classification of articles (eg: maternity) 
    List<String> brand = Arrays.asList(); // List<String> | filters by brand key given by user (eg: SA5)
    List<String> brandfamily = Arrays.asList(); // List<String> | filters by brand family key (eg: nike) 
    List<String> category = Arrays.asList(); // List<String> | filters by category (eg: Socks, Rain Coats)
    List<String> color = Arrays.asList(); // List<String> | filters by color (eg: red, blue)
    List<String> den = Arrays.asList(); // List<String> | filters by den 
    List<String> filling = Arrays.asList(); // List<String> | filters by different kinds of garment filling materials (eg: satin, wolle)
    List<String> gender = Arrays.asList(); // List<String> | filters by gender
    List<String> heelForm = Arrays.asList(); // List<String> | filters by heel form (eg: flat)
    List<String> heelHeight = Arrays.asList(); // List<String> | filters by height of the heel size or length (eg: xs)
    String length = "length_example"; // String | filters by garments length (eg: 3/4 length, knee-length)
    List<String> occasion = Arrays.asList(); // List<String> | filters by type of occasion (eg: party, business)
    List<String> pattern = Arrays.asList(); // List<String> | filters by pattern on the garments (eg: animal print, plain)
    String price = "price_example"; // String | filters all articles in price range (eg: 9-90)
    List<String> sale = Arrays.asList(); // List<String> | filters discounted articles marked as sale
    List<String> season = Arrays.asList(); // List<String> | filters by season (Autumn/Winter or Spring/Summer)
    List<String> shaftHeight = Arrays.asList(); // List<String> | filters by shaft height (eg: s, xs)
    List<String> shaftWidth = Arrays.asList(); // List<String> | filters by shaft width (eg: s, l)
    List<String> shirtCollar = Arrays.asList(); // List<String> | filters by shirt collar styles (eg: low V neck, lined collar)
    List<String> shoeFastener = Arrays.asList(); // List<String> | filters by shoe fastener types (eg: buckle, lacing)
    List<String> shoeToecap = Arrays.asList(); // List<String> | filters by shoe toe cap variants (eg: pointed, square)
    List<String> shopArea = Arrays.asList(); // List<String> | filters by classification of articles
    String size = "size_example"; // String | filters by size
    List<String> sports = Arrays.asList(); // List<String> | filters by different sport activities (eg: football)
    List<String> technology = Arrays.asList(); // List<String> | filters by technology used to produce the articles
    List<String> trouserRise = Arrays.asList(); // List<String> | filters by trouser rise
    List<String> upperMaterial = Arrays.asList(); // List<String> | filters by different type of upper material used on garments (eg: lace)
    List<String> volume = Arrays.asList(); // List<String> | filters by volume
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      List<Facet> result = apiInstance.facetsGet(ageGroup, articleId, activationDate, articleModelId, assortmentArea, brand, brandfamily, category, color, den, filling, gender, heelForm, heelHeight, length, occasion, pattern, price, sale, season, shaftHeight, shaftWidth, shirtCollar, shoeFastener, shoeToecap, shopArea, size, sports, technology, trouserRise, upperMaterial, volume, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacetsApi#facetsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ageGroup** | [**List&lt;String&gt;**](String.md)| filters by age group (eg: kids) | [optional] [enum: babies, kids, teen, adult] |
| **articleId** | [**List&lt;String&gt;**](String.md)| The &#x60;articleIds&#x60; to use use for filtering.  One or more &#x60;articleIds&#x60; might be used as a filter criteria. Submit multiple &#x60;articleId&#x60; request parameters for more than one to be used. They will be treated as &#x60;OR&#x60; criteria. | [optional] |
| **activationDate** | [**List&lt;String&gt;**](String.md)| period or time the articles are activated for selling in the shop | [optional] [enum: thisWeek, lastWeek, lastMonth] |
| **articleModelId** | [**List&lt;String&gt;**](String.md)| filters by article ModelId | [optional] |
| **assortmentArea** | [**List&lt;String&gt;**](String.md)| filters by classification of articles (eg: maternity)  | [optional] [enum: standard, maternity, plusSize, petite] |
| **brand** | [**List&lt;String&gt;**](String.md)| filters by brand key given by user (eg: SA5) | [optional] |
| **brandfamily** | [**List&lt;String&gt;**](String.md)| filters by brand family key (eg: nike)  | [optional] |
| **category** | [**List&lt;String&gt;**](String.md)| filters by category (eg: Socks, Rain Coats) | [optional] |
| **color** | [**List&lt;String&gt;**](String.md)| filters by color (eg: red, blue) | [optional] [enum: black, brown, beige, gray, white, blue, petrol, turquoise, green, olive, yellow, orange, red, pink, purple, gold, silver, multicolored] |
| **den** | [**List&lt;String&gt;**](String.md)| filters by den  | [optional] [enum: den15, den20, den40, den60, den80, den100, den200, den120, den12, den50] |
| **filling** | [**List&lt;String&gt;**](String.md)| filters by different kinds of garment filling materials (eg: satin, wolle) | [optional] [enum: angora, baumwolle, daunen, fell, fleece, frottee, kaschmir, lammfell, leder, lederimitat, merinowolle, microfaser, mohair, satin, schurwolle, seide, sonstige, textil, warm, wolle] |
| **gender** | [**List&lt;String&gt;**](String.md)| filters by gender | [optional] [enum: male, female] |
| **heelForm** | [**List&lt;String&gt;**](String.md)| filters by heel form (eg: flat) | [optional] [enum: block, flat, wedge, penny, funnel, plateau, plateauBoots, wedgeHidden, plateauHidden, plateauHeels] |
| **heelHeight** | [**List&lt;String&gt;**](String.md)| filters by height of the heel size or length (eg: xs) | [optional] [enum: xs, s, m] |
| **length** | **String**| filters by garments length (eg: 3/4 length, knee-length) | [optional] |
| **occasion** | [**List&lt;String&gt;**](String.md)| filters by type of occasion (eg: party, business) | [optional] [enum: business, octoberFest, loungeWear, evening, party, leisure] |
| **pattern** | [**List&lt;String&gt;**](String.md)| filters by pattern on the garments (eg: animal print, plain) | [optional] [enum: animalPrint, checkered, colored, floral, polkaDot, striped, paisley, plain, print, burnout, herringBone, camouflage, flecked, pinstripe, gradient, photoPrint] |
| **price** | **String**| filters all articles in price range (eg: 9-90) | [optional] |
| **sale** | [**List&lt;String&gt;**](String.md)| filters discounted articles marked as sale | [optional] [enum: sale] |
| **season** | [**List&lt;String&gt;**](String.md)| filters by season (Autumn/Winter or Spring/Summer) | [optional] [enum: winter, summer] |
| **shaftHeight** | [**List&lt;String&gt;**](String.md)| filters by shaft height (eg: s, xs) | [optional] [enum: xs, s, m, l] |
| **shaftWidth** | [**List&lt;String&gt;**](String.md)| filters by shaft width (eg: s, l) | [optional] [enum: s, m, l] |
| **shirtCollar** | [**List&lt;String&gt;**](String.md)| filters by shirt collar styles (eg: low V neck, lined collar) | [optional] [enum: lapelCollar, mandarinCollar, hood, poloNeck, poloShirt, cowlNeck, roundNeck, scarfCollar, boatNeck, vNeck, buttonDown, turnDownCollar, highCollar, linedCollar, shirtCollar, cutawayCollar, doubleCollar, peterPanCollar, kentCollar, cupShapedCollar, contrastCollar, maoCollar, wingCollar, tabCollar, volantCollar, shawlCollar, envelope, lowVNeck, cacheCeour, lowRoundNeck, backless, henley, squareNeck, offTheShoulder] |
| **shoeFastener** | [**List&lt;String&gt;**](String.md)| filters by shoe fastener types (eg: buckle, lacing) | [optional] [enum: buckle, belt, lacing, open, zipper, velcro] |
| **shoeToecap** | [**List&lt;String&gt;**](String.md)| filters by shoe toe cap variants (eg: pointed, square) | [optional] [enum: round, pointed, open, square] |
| **shopArea** | [**List&lt;String&gt;**](String.md)| filters by classification of articles | [optional] [enum: shop, sale] |
| **size** | **String**| filters by size | [optional] |
| **sports** | [**List&lt;String&gt;**](String.md)| filters by different sport activities (eg: football) | [optional] [enum: outdoor, skiSnow, running, training, football, handball, basketball, volleyball, golf, tennis, beach, skate, riding, cycling, sailing, badminton, dancing, snowboard, swimming] |
| **technology** | [**List&lt;String&gt;**](String.md)| filters by technology used to produce the articles | [optional] [enum: clima365, climacool, climalite, climaproof, climawarm, driFit, flywire, formotion, omniHeat, polartec, primaloft, staywarm, techfit, thinsulate, venturi, h2no, dermizax, performanceShell, softShell, windstopper, proShell, hydratic, pacliteShell, activeShell, goreTex, hyvent, texapore, precip] |
| **trouserRise** | [**List&lt;String&gt;**](String.md)| filters by trouser rise | [optional] [enum: high, medium, low] |
| **upperMaterial** | [**List&lt;String&gt;**](String.md)| filters by different type of upper material used on garments (eg: lace) | [optional] [enum: batiste, caoutchouc, cashmere, damask, down, feathers, felt, flanelette, flannel, fleece, imitationLeather, jacquard, jersey, leather, linen, linon, mesh, microfiber, mohair, other, percale, polyester, renforce, satin, seersucker, silk, synthetic, textile, towelling, varnish, velours, viscose, wool, cord, denim, rib, braided, crocheted, hardshell, softshell, lace, sweat] |
| **volume** | [**List&lt;String&gt;**](String.md)| filters by volume | [optional] [enum: smallest, small, medium, large, largest] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**List&lt;Facet&gt;**](Facet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Facets response. |  -  |
| **400** | Bad request. |  -  |

