/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICountryVO.h
 *
 * Java type: com.noosh.nooshapi.vo.CountryVO
 */

#ifndef OAICountryVO_H
#define OAICountryVO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICountryVO : public OAIObject {
public:
    OAICountryVO();
    OAICountryVO(QString json);
    ~OAICountryVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getConstantToken() const;
    void setConstantToken(const QString &constant_token);
    bool is_constant_token_Set() const;
    bool is_constant_token_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    qint64 getCountryId() const;
    void setCountryId(const qint64 &country_id);
    bool is_country_id_Set() const;
    bool is_country_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_constant_token;
    bool m_constant_token_isSet;
    bool m_constant_token_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    qint64 m_country_id;
    bool m_country_id_isSet;
    bool m_country_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICountryVO)

#endif // OAICountryVO_H
