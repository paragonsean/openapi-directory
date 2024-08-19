/*
 * カラーミーショップアプリストア API
 * # カラーミーショップアプリストア API  [アプリストア](https://app.shop-pro.jp/)にて公開するアプリに対して、一般公開している[カラーミーショップAPI](https://developer.shop-pro.jp/docs/colorme-api)に加えて、カラーミーショップアプリストアAPI（以下、アプリストアAPIといいます）を利用することが出来ます。アプリストアAPIでは以下のことが行えます。 - 課金データ(アプリ内課金、従量課金)の作成 - インラインスクリプトタグの取得・作成・更新・削除 - スクリプトタグの取得・作成・更新・削除  ## 利用手順  アプリストアAPIを利用するには、OAuth認証が必要です。OAuth認証の基本的な流れについては[カラーミーショップAPIドキュメント](https://developer.shop-pro.jp/docs/colorme-api)を参照してください。 アプリストアAPIの利用のために、以下のscopeが追加で指定可能になります。[カラーミーショップAPIドキュメント](https://developer.shop-pro.jp/docs/colorme-api)に掲載されているscopeと合わせてご利用ください。  |スコープ|機能| |---|---| |`write_application_charge`|課金データの作成| |`read_shop_script_tags`|ショップページのスクリプトタグを参照| |`write_shop_script_tags`|ショップページへスクリプトタグを追加・更新| |`read_inline_script_tags`|インラインスクリプトタグを参照| |`write_inline_script_tags`|インラインスクリプトタグを追加・更新| |`read_script_tags`|スクリプトタグを参照(deprecated)| |`write_script_tags`|スクリプトタグを追加・更新(deprecated)|  (例) カラーミーショップアカウントの認証ページを表示 ``` https://api.shop-pro.jp/oauth/authorize?client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&response_type=code&scope=read_products%20write_products%20write_application_charge ```  ## 課金設定 料金プラン（月額課金・従量課金・買い切り）による課金や、アプリ内課金をご利用いただくにはアプリごとに課金設定の登録が必要です。 この設定は [カラーミーショップ デベロッパー](https://developer.shop-pro.jp) から行うことができます。  登録できる課金形式やその使い方の詳細については[アプリストア 開発ガイドのアプリ課金のページ](https://developer.shop-pro.jp/getting-started/appstore-billing/)をご覧ください  ## アプリのインストール ショップオーナーがアプリをインストールしたとき、以下の処理をカラーミーショップが行います。 - 選択された料金プランに基づき課金開始 - インストールフックの呼び出し  ### インストールフック アプリのインストール時に、インストールに関する情報を `POST` メソッド、 `application/json` 形式で通知します。 通知先のURLは[カラーミーショップ デベロッパー](https://developer.shop-pro.jp/)にログインし、各アプリストア アプリのアプリ設定から登録を行ってください。  以下のパラメータが送信されます。課金請求に必要なパラメータを含みますので、必ず受け取れるようにしてください。  |パラメータ|機能|形式| |---|---|---| |`account_id`|インストールしたショップオーナーのアカウントID|PA+8桁の整数| |`application_charge_source_id`|プラン課金ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`recurring_application_charge_id`|（買い切り以外の課金の場合）課金契約ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`application_charge_id`|（買い切りの場合）課金契約ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`trial_term`|（無料お試し期間がある場合）無料お試し期間|JSONオブジェクト| |`mail`|ショップオーナーへの連絡メールアドレス|文字列|  `application_charge_source_id` はデベロッパーサイトで設定したプラン課金のIDです。インストールされた料金プランの判別にご利用いただけます。  `recurring_application_charge_id` と `application_charge_id` はインストールごとに発行されるユニークなIDです。ショップオーナーが一度アンインストールした後に、再度同じショップオーナーがアプリのインストールを行った際には新たに別のIDが発行されます。  `recurring_application_charge_id` は「買い切り」以外の課金である「無料」「月額」「月額＋従量」「月額＋初期費用」「従量のみ」のプラン課金のインストールの際に発行されます。  従量による課金を伴うプラン課金の場合は、従量分の料金を請求する際に 課金契約ID(`recurring_application_charge_id`) が必要になるので、必ず記録するようにしてください。  `mail` パラメータの値はショップオーナーへの連絡手段としてご利用いただけます。インストール後に認可フローが中断され、アクセストークンが得られない際のショップオーナーへの連絡手段としてご活用いただけます。このパラメータはカラーミーショップの非公開情報として登録されている値です。左記以外の用途でこの値をアプリの機能で使用しないでください。  例) 買い切りの場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"F3RN9A\",   \"application_charge_id\": \"A3FT4N\",   \"mail\": \"shop@example.com\" } ```  例) 月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"F3RN9A\",   \"recurring_application_charge_id\": \"A3FT4N\",   \"mail\": \"shop@example.com\" } ```  無料お試し期間を設定した課金の場合、以下の情報を `trial_term` パラメータとして送信します。 無料お試し期間中は従量課金APIを呼び出して課金請求することはできません。  |パラメータ|機能|形式| |---|---|---| |`starts_at`|無料お試し開始日時|整数値(UNIXタイムスタンプ)| |`ends_at`|無料お試し終了日時|整数値(UNIXタイムスタンプ)|  例) 無料お試し期間がある月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"F3RN9A\",   \"recurring_application_charge_id\": \"A3FT4N\",   \"mail\": \"shop@example.com\",   \"trial_term\" {     \"starts_at\": 1565017200,     \"ends_at\": 1567609200   } } ```  受け取りに成功した場合は、以下のパラメータを `application/json` 形式でレスポンスボディに付与し、 ステータスコード `200` レスポンスをカラーミーショップへ返却してください。 ステータスコード `200` レスポンスをカラーミーショップが受け取れない場合、もしくは以下のパラメーターが返却されなかった場合、インストールを中止し、インストールによって発生した情報は破棄されます。  |パラメータ|機能|形式| |---|---|---| |`redirect_url`|インストール成功後に遷移するURL|文字列（URL）|  例) ``` {   \"redirect_url\": \"https://example.com\" } ``` インストール完了後、インストールフックのレスポンスパラメータの `redirect_url` へ画面遷移しますので、APIを利用する場合は `redirect_url` より先の画面でOAuth認証の実装をお願いします。  ## アプリのアンインストール ショップオーナーがアプリをアンインストールしたとき、以下の処理をカラーミーショップが行います。 - OAuth認証のアクセストークンの無効化 - 登録したインラインスクリプトタグ・スクリプトタグの削除 - 月額課金形式の場合、継続課金の無効化  ### アンインストールフック アンインストール直後に `POST` メソッドで、以下の情報を `application/json` 形式で通知します。 通知先のURLは[カラーミーショップ デベロッパー](https://developer.shop-pro.jp/)にログインし、各アプリストア アプリのアプリ設定から登録を行ってください。  ※ [アンインストールAPI](#operation/deleteInstallation)のご利用によるアンインストール時はアンインストールフックは通知されません。  受け取りに成功した場合はステータスコード `200` のレスポンスを返却してください。  |パラメータ|機能|形式| |---|---|---| |`account_id`|アンインストールしたショップオーナーのアカウントID|PA+8桁の整数| |`application_charge_source_id`|プラン課金ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`uninstalled_at`|アンインストール日時|整数値(UNIXタイムスタンプ)| |`reason`|アンインストール理由| `by_shop_owner` (ショップオーナーによる)<br /> `by_unpaid` (未払いによる) | |`recurring_application_charge_id`|（買い切り以外の課金の場合）課金契約ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`usage_charge`|（従量課金の場合）従量課金アンインストール情報|JSONオブジェクト|  アンインストールフックの通知が伴うアンインストールは以下の操作のいずれかによって行われます。アンインストールの理由を `reason` パラメータで確認できます。  |reasonパラメータの値|アンインストール理由| |---|---| |`by_shop_owner`|ショップオーナーによるアンインストール操作| |`by_unpaid`|ポイント不足による利用料徴収の失敗による自動アンインストール|  課金契約ID `recurring_application_charge_id` はインストールフックで通知したIDと同じIDが通知されます。  料金プランが従量課金の場合、アンインストール後に従量課金データの作成を可能にするために、以下の情報を `usage_charge` パラメータとして送信します。 アンインストール後はOAuthのアクセストークンが無効化されているため、アクセストークンを利用して従量課金APIを呼び出すことができなくなります。 アンインストール後はアクセストークンの代わりに `api_token` をリクエストヘッダーに含め、従量課金APIを呼び出してください。 無料お試し期間中にアプリがアンインストールされた場合は、`api_token` は発行されません。 詳しくは、[従量課金データの作成](https://app.shop-pro.jp/open_api#operation/createUsageCharge)を参照してください。 `api_token` を利用した従量課金APIの呼び出しは、ポイント締め日 `closing_on` までとなっておりますので、ご注意ください。  |パラメータ|機能|形式| |---|---|---| |`api_token`|アンインストール後に従量課金APIを利用いただくために必要な情報|文字列| |`closing_on`|ポイント締め日|整数値(UNIXタイムスタンプ)|  通常、 `closing_on` は、アンインストール直前まで利用されていた契約の期間の月末となります。以下に例を示します。  |アンインストール日|直前まで利用されていた契約の期間|closing_on の示す日時| |---|---|---| |2021/01/09|2021/12/10〜2021/01/09|2021/01/31| |2021/01/10|2021/01/10〜2021/02/09|2021/02/28|  従量課金の場合のユーザーの契約期間については[こちら](https://shop-pro.jp/manual/appstore_fee)をご参照ください  アンインストールフックの例を以下に示します。  例) 買い切りの場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"Q21GPC\",   \"uninstalled_at\": 1552022739,   \"reason\": \"by_shop_owner\" } ```  例) 月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"EW3V21\",   \"recurring_application_charge_id\": \"F3RN9A\",   \"uninstalled_at\": 1552022740,   \"reason\": \"by_shop_owner\" } ```  例) 従量課金を含む月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"WA37CA\",   \"recurring_application_charge_id\": \"F3WQ1S\",   \"uninstalled_at\": 1552022740,   \"reason\": \"by_shop_owner\",   \"usage_charge\": {     \"api_token\": \"token\",     \"closing_on\": 1552533465   } } ```  ### アンインストールフックのリトライ ステータスコード `200` のレスポンスをカラーミーショップが受け取れない場合は、ステータスコード `200` をカラーミーショップが受け取るまで、以下の条件で再度アンインストール情報を送信します。 なお、カラーミーショップによるアンインストール処理は、アンインストールフックの送信結果の成否によらず、アンインストールが実行されたときに完了します。  - 2時間30分ごとにアンインストールフックの仕様に基づき再送します - 最大で合計19回再送します - すべての再送の試行でステータスコード `200` をカラーミーショップが受け取れない場合は、公認デベロッパー申請時に登録されたメールアドレス宛にメールを送信します  ## インストール・アンインストールフックの署名検証 `X-Appstore-Signature` リクエストヘッダーに含まれる署名を検証して、リクエストがカラーミーショップから送信されたことを確認することを推奨します。  検証の手順は以下のとおりです。  1. カラーミーショップが発行した `webhook_secret` を秘密鍵として、HMAC-SHA256アルゴリズムを使用してリクエストボディのダイジェスト値を取得します。 2. ダイジェスト値をBase64エンコードした値とリクエストヘッダーに付与された署名( `X-Appstore-Signature` の値）が一致することを確認します。   サンプルコード(ruby) ```ruby WEBHOOK_SECRET = 'my_webhook_secret'  payload_body = request.body.read signature = Base64.strict_encode64(OpenSSL::HMAC.digest('sha256', WEBHOOK_SECRET, payload_body)) ActiveSupport::SecurityUtils.secure_compare(signature, request.env['HTTP_X_APPSTORE_SIGNATURE']) ```  ### 発信元IPアドレスについて  発信元IPアドレスは固定ではありません。そのためIPアドレスが固定されていることを前提としてアプリケーションを開発しないでください。  インストールフックおよびアンインストールフックのリクエストの発信元を検証する場合は上記の署名検証を行なってください。 
 *
 * The version of the OpenAPI document: 1.0.0
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
import java.util.Arrays;

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
 * InlineScriptTag
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:30:55.197839-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InlineScriptTag {
  public static final String SERIALIZED_NAME_ACCOUNT_ID = "account_id";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_ID)
  private String accountId;

  /**
   * インラインスクリプトを出力するページ。  - &#x60;all&#x60;: カートの途中のページと注文完了ページの両方 - &#x60;thanks_page&#x60;: 注文完了ページ - &#x60;cart&#x60;: カートの途中のページ 
   */
  @JsonAdapter(DisplayScopeEnum.Adapter.class)
  public enum DisplayScopeEnum {
    ALL("all"),
    
    THANKS_PAGE("thanks_page"),
    
    CART("cart");

    private String value;

    DisplayScopeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DisplayScopeEnum fromValue(String value) {
      for (DisplayScopeEnum b : DisplayScopeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DisplayScopeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DisplayScopeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DisplayScopeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DisplayScopeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DisplayScopeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DISPLAY_SCOPE = "display_scope";
  @SerializedName(SERIALIZED_NAME_DISPLAY_SCOPE)
  private DisplayScopeEnum displayScope;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_MAKE_DATE = "make_date";
  @SerializedName(SERIALIZED_NAME_MAKE_DATE)
  private Integer makeDate;

  public static final String SERIALIZED_NAME_OAUTH_APPLICATION_ID = "oauth_application_id";
  @SerializedName(SERIALIZED_NAME_OAUTH_APPLICATION_ID)
  private Integer oauthApplicationId;

  public static final String SERIALIZED_NAME_SCRIPT = "script";
  @SerializedName(SERIALIZED_NAME_SCRIPT)
  private String script;

  /**
   * インラインスクリプトを実行するタイミング。  - &#x60;object_builded&#x60;: JSオブジェクトの作成が完了した時 
   */
  @JsonAdapter(TriggerEventEnum.Adapter.class)
  public enum TriggerEventEnum {
    OBJECT_BUILDED("object_builded");

    private String value;

    TriggerEventEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TriggerEventEnum fromValue(String value) {
      for (TriggerEventEnum b : TriggerEventEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TriggerEventEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TriggerEventEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TriggerEventEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TriggerEventEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TriggerEventEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TRIGGER_EVENT = "trigger_event";
  @SerializedName(SERIALIZED_NAME_TRIGGER_EVENT)
  private TriggerEventEnum triggerEvent;

  public static final String SERIALIZED_NAME_UPDATE_DATE = "update_date";
  @SerializedName(SERIALIZED_NAME_UPDATE_DATE)
  private Integer updateDate;

  public InlineScriptTag() {
  }

  public InlineScriptTag accountId(String accountId) {
    this.accountId = accountId;
    return this;
  }

  /**
   * アカウントID
   * @return accountId
   */
  @javax.annotation.Nullable
  public String getAccountId() {
    return accountId;
  }

  public void setAccountId(String accountId) {
    this.accountId = accountId;
  }


  public InlineScriptTag displayScope(DisplayScopeEnum displayScope) {
    this.displayScope = displayScope;
    return this;
  }

  /**
   * インラインスクリプトを出力するページ。  - &#x60;all&#x60;: カートの途中のページと注文完了ページの両方 - &#x60;thanks_page&#x60;: 注文完了ページ - &#x60;cart&#x60;: カートの途中のページ 
   * @return displayScope
   */
  @javax.annotation.Nullable
  public DisplayScopeEnum getDisplayScope() {
    return displayScope;
  }

  public void setDisplayScope(DisplayScopeEnum displayScope) {
    this.displayScope = displayScope;
  }


  public InlineScriptTag id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * インラインスクリプトタグID
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public InlineScriptTag makeDate(Integer makeDate) {
    this.makeDate = makeDate;
    return this;
  }

  /**
   * 作成日時
   * @return makeDate
   */
  @javax.annotation.Nullable
  public Integer getMakeDate() {
    return makeDate;
  }

  public void setMakeDate(Integer makeDate) {
    this.makeDate = makeDate;
  }


  public InlineScriptTag oauthApplicationId(Integer oauthApplicationId) {
    this.oauthApplicationId = oauthApplicationId;
    return this;
  }

  /**
   * アプリID
   * @return oauthApplicationId
   */
  @javax.annotation.Nullable
  public Integer getOauthApplicationId() {
    return oauthApplicationId;
  }

  public void setOauthApplicationId(Integer oauthApplicationId) {
    this.oauthApplicationId = oauthApplicationId;
  }


  public InlineScriptTag script(String script) {
    this.script = script;
    return this;
  }

  /**
   * インラインスクリプト
   * @return script
   */
  @javax.annotation.Nullable
  public String getScript() {
    return script;
  }

  public void setScript(String script) {
    this.script = script;
  }


  public InlineScriptTag triggerEvent(TriggerEventEnum triggerEvent) {
    this.triggerEvent = triggerEvent;
    return this;
  }

  /**
   * インラインスクリプトを実行するタイミング。  - &#x60;object_builded&#x60;: JSオブジェクトの作成が完了した時 
   * @return triggerEvent
   */
  @javax.annotation.Nullable
  public TriggerEventEnum getTriggerEvent() {
    return triggerEvent;
  }

  public void setTriggerEvent(TriggerEventEnum triggerEvent) {
    this.triggerEvent = triggerEvent;
  }


  public InlineScriptTag updateDate(Integer updateDate) {
    this.updateDate = updateDate;
    return this;
  }

  /**
   * 更新日時
   * @return updateDate
   */
  @javax.annotation.Nullable
  public Integer getUpdateDate() {
    return updateDate;
  }

  public void setUpdateDate(Integer updateDate) {
    this.updateDate = updateDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InlineScriptTag inlineScriptTag = (InlineScriptTag) o;
    return Objects.equals(this.accountId, inlineScriptTag.accountId) &&
        Objects.equals(this.displayScope, inlineScriptTag.displayScope) &&
        Objects.equals(this.id, inlineScriptTag.id) &&
        Objects.equals(this.makeDate, inlineScriptTag.makeDate) &&
        Objects.equals(this.oauthApplicationId, inlineScriptTag.oauthApplicationId) &&
        Objects.equals(this.script, inlineScriptTag.script) &&
        Objects.equals(this.triggerEvent, inlineScriptTag.triggerEvent) &&
        Objects.equals(this.updateDate, inlineScriptTag.updateDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountId, displayScope, id, makeDate, oauthApplicationId, script, triggerEvent, updateDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineScriptTag {\n");
    sb.append("    accountId: ").append(toIndentedString(accountId)).append("\n");
    sb.append("    displayScope: ").append(toIndentedString(displayScope)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    makeDate: ").append(toIndentedString(makeDate)).append("\n");
    sb.append("    oauthApplicationId: ").append(toIndentedString(oauthApplicationId)).append("\n");
    sb.append("    script: ").append(toIndentedString(script)).append("\n");
    sb.append("    triggerEvent: ").append(toIndentedString(triggerEvent)).append("\n");
    sb.append("    updateDate: ").append(toIndentedString(updateDate)).append("\n");
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
    openapiFields.add("account_id");
    openapiFields.add("display_scope");
    openapiFields.add("id");
    openapiFields.add("make_date");
    openapiFields.add("oauth_application_id");
    openapiFields.add("script");
    openapiFields.add("trigger_event");
    openapiFields.add("update_date");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InlineScriptTag
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InlineScriptTag.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InlineScriptTag is not found in the empty JSON string", InlineScriptTag.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InlineScriptTag.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InlineScriptTag` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("account_id") != null && !jsonObj.get("account_id").isJsonNull()) && !jsonObj.get("account_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `account_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("account_id").toString()));
      }
      if ((jsonObj.get("display_scope") != null && !jsonObj.get("display_scope").isJsonNull()) && !jsonObj.get("display_scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_scope").toString()));
      }
      // validate the optional field `display_scope`
      if (jsonObj.get("display_scope") != null && !jsonObj.get("display_scope").isJsonNull()) {
        DisplayScopeEnum.validateJsonElement(jsonObj.get("display_scope"));
      }
      if ((jsonObj.get("script") != null && !jsonObj.get("script").isJsonNull()) && !jsonObj.get("script").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `script` to be a primitive type in the JSON string but got `%s`", jsonObj.get("script").toString()));
      }
      if ((jsonObj.get("trigger_event") != null && !jsonObj.get("trigger_event").isJsonNull()) && !jsonObj.get("trigger_event").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `trigger_event` to be a primitive type in the JSON string but got `%s`", jsonObj.get("trigger_event").toString()));
      }
      // validate the optional field `trigger_event`
      if (jsonObj.get("trigger_event") != null && !jsonObj.get("trigger_event").isJsonNull()) {
        TriggerEventEnum.validateJsonElement(jsonObj.get("trigger_event"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InlineScriptTag.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InlineScriptTag' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InlineScriptTag> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InlineScriptTag.class));

       return (TypeAdapter<T>) new TypeAdapter<InlineScriptTag>() {
           @Override
           public void write(JsonWriter out, InlineScriptTag value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InlineScriptTag read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InlineScriptTag given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InlineScriptTag
   * @throws IOException if the JSON string is invalid with respect to InlineScriptTag
   */
  public static InlineScriptTag fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InlineScriptTag.class);
  }

  /**
   * Convert an instance of InlineScriptTag to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

