/**
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISuccess_Upsell.h
 *
 * 
 */

#ifndef OAISuccess_Upsell_H
#define OAISuccess_Upsell_H

#include <QJsonObject>

#include "OAICollection_Meta_Upsell.h"
#include "OAIDictionaries.h"
#include "OAIFlightOffer.h"
#include "OAIIssue.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFlightOffer;
class OAIDictionaries;
class OAICollection_Meta_Upsell;
class OAIIssue;

class OAISuccess_Upsell : public OAIObject {
public:
    OAISuccess_Upsell();
    OAISuccess_Upsell(QString json);
    ~OAISuccess_Upsell() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIFlightOffer> getData() const;
    void setData(const QList<OAIFlightOffer> &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    OAIDictionaries getDictionaries() const;
    void setDictionaries(const OAIDictionaries &dictionaries);
    bool is_dictionaries_Set() const;
    bool is_dictionaries_Valid() const;

    OAICollection_Meta_Upsell getMeta() const;
    void setMeta(const OAICollection_Meta_Upsell &meta);
    bool is_meta_Set() const;
    bool is_meta_Valid() const;

    QList<OAIIssue> getWarnings() const;
    void setWarnings(const QList<OAIIssue> &warnings);
    bool is_warnings_Set() const;
    bool is_warnings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIFlightOffer> m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    OAIDictionaries m_dictionaries;
    bool m_dictionaries_isSet;
    bool m_dictionaries_isValid;

    OAICollection_Meta_Upsell m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;

    QList<OAIIssue> m_warnings;
    bool m_warnings_isSet;
    bool m_warnings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISuccess_Upsell)

#endif // OAISuccess_Upsell_H
