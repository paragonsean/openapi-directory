/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDealerDB_Models_DealersPerCountry.h
 *
 * 
 */

#ifndef OAIDealerDB_Models_DealersPerCountry_H
#define OAIDealerDB_Models_DealersPerCountry_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDealerDB_Models_DealersPerCountry : public OAIObject {
public:
    OAIDealerDB_Models_DealersPerCountry();
    OAIDealerDB_Models_DealersPerCountry(QString json);
    ~OAIDealerDB_Models_DealersPerCountry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCount() const;
    void setCount(const qint32 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDealerDB_Models_DealersPerCountry)

#endif // OAIDealerDB_Models_DealersPerCountry_H
