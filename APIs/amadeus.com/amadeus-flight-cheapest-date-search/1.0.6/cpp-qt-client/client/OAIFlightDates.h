/**
 * Flight Cheapest Date Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.6
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFlightDates.h
 *
 * 
 */

#ifndef OAIFlightDates_H
#define OAIFlightDates_H

#include <QJsonObject>

#include "OAIDictionaries.h"
#include "OAIFlightDate.h"
#include "OAIIssue.h"
#include "OAIMeta.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFlightDate;
class OAIDictionaries;
class OAIMeta;
class OAIIssue;

class OAIFlightDates : public OAIObject {
public:
    OAIFlightDates();
    OAIFlightDates(QString json);
    ~OAIFlightDates() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIFlightDate> getData() const;
    void setData(const QList<OAIFlightDate> &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    OAIDictionaries getDictionaries() const;
    void setDictionaries(const OAIDictionaries &dictionaries);
    bool is_dictionaries_Set() const;
    bool is_dictionaries_Valid() const;

    OAIMeta getMeta() const;
    void setMeta(const OAIMeta &meta);
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

    QList<OAIFlightDate> m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    OAIDictionaries m_dictionaries;
    bool m_dictionaries_isSet;
    bool m_dictionaries_isValid;

    OAIMeta m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;

    QList<OAIIssue> m_warnings;
    bool m_warnings_isSet;
    bool m_warnings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFlightDates)

#endif // OAIFlightDates_H
