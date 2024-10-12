/**
 * Trip Purpose Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.1.4
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDefaults.h
 *
 * the query parameters for which default values were used are returned here
 */

#ifndef OAIDefaults_H
#define OAIDefaults_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDefaults : public OAIObject {
public:
    OAIDefaults();
    OAIDefaults(QString json);
    ~OAIDefaults() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getSearchDate() const;
    void setSearchDate(const QString &search_date);
    bool is_search_date_Set() const;
    bool is_search_date_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_search_date;
    bool m_search_date_isSet;
    bool m_search_date_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDefaults)

#endif // OAIDefaults_H
