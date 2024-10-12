/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAML.h
 *
 * 
 */

#ifndef OAIAML_H
#define OAIAML_H

#include <QJsonObject>

#include "OAIAML_address_inner.h"
#include "OAIAML_aliases_inner.h"
#include "OAIAML_passport_inner.h"
#include "OAISelfLink.h"
#include <QDate>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISelfLink;
class OAIAML_address_inner;
class OAIAML_aliases_inner;
class OAIAML_passport_inner;

class OAIAML : public OAIObject {
public:
    OAIAML();
    OAIAML(QString json);
    ~OAIAML() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAISelfLink> getLinks() const;
    void setLinks(const QList<OAISelfLink> &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    QList<OAIAML_address_inner> getAddress() const;
    void setAddress(const QList<OAIAML_address_inner> &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QList<OAIAML_aliases_inner> getAliases() const;
    void setAliases(const QList<OAIAML_aliases_inner> &aliases);
    bool is_aliases_Set() const;
    bool is_aliases_Valid() const;

    QString getComments() const;
    void setComments(const QString &comments);
    bool is_comments_Set() const;
    bool is_comments_Valid() const;

    QString getConfidence() const;
    void setConfidence(const QString &confidence);
    bool is_confidence_Set() const;
    bool is_confidence_Valid() const;

    QList<QDate> getDob() const;
    void setDob(const QList<QDate> &dob);
    bool is_dob_Set() const;
    bool is_dob_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QList<QString> getLegalBasis() const;
    void setLegalBasis(const QList<QString> &legal_basis);
    bool is_legal_basis_Set() const;
    bool is_legal_basis_Valid() const;

    QString getNationality() const;
    void setNationality(const QString &nationality);
    bool is_nationality_Set() const;
    bool is_nationality_Valid() const;

    QList<OAIAML_passport_inner> getPassport() const;
    void setPassport(const QList<OAIAML_passport_inner> &passport);
    bool is_passport_Set() const;
    bool is_passport_Valid() const;

    QString getRegime() const;
    void setRegime(const QString &regime);
    bool is_regime_Set() const;
    bool is_regime_Valid() const;

    QString getSource() const;
    void setSource(const QString &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    QString getSourceType() const;
    void setSourceType(const QString &source_type);
    bool is_source_type_Set() const;
    bool is_source_type_Valid() const;

    QList<QString> getTitle() const;
    void setTitle(const QList<QString> &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAISelfLink> m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    QList<OAIAML_address_inner> m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QList<OAIAML_aliases_inner> m_aliases;
    bool m_aliases_isSet;
    bool m_aliases_isValid;

    QString m_comments;
    bool m_comments_isSet;
    bool m_comments_isValid;

    QString m_confidence;
    bool m_confidence_isSet;
    bool m_confidence_isValid;

    QList<QDate> m_dob;
    bool m_dob_isSet;
    bool m_dob_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QList<QString> m_legal_basis;
    bool m_legal_basis_isSet;
    bool m_legal_basis_isValid;

    QString m_nationality;
    bool m_nationality_isSet;
    bool m_nationality_isValid;

    QList<OAIAML_passport_inner> m_passport;
    bool m_passport_isSet;
    bool m_passport_isValid;

    QString m_regime;
    bool m_regime_isSet;
    bool m_regime_isValid;

    QString m_source;
    bool m_source_isSet;
    bool m_source_isValid;

    QString m_source_type;
    bool m_source_type_isSet;
    bool m_source_type_isValid;

    QList<QString> m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAML)

#endif // OAIAML_H
