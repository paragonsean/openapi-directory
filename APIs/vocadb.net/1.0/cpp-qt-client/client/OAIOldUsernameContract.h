/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOldUsernameContract.h
 *
 * 
 */

#ifndef OAIOldUsernameContract_H
#define OAIOldUsernameContract_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOldUsernameContract : public OAIObject {
public:
    OAIOldUsernameContract();
    OAIOldUsernameContract(QString json);
    ~OAIOldUsernameContract() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getDate() const;
    void setDate(const QDateTime &date);
    bool is_date_Set() const;
    bool is_date_Valid() const;

    QString getOldName() const;
    void setOldName(const QString &old_name);
    bool is_old_name_Set() const;
    bool is_old_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_date;
    bool m_date_isSet;
    bool m_date_isValid;

    QString m_old_name;
    bool m_old_name_isSet;
    bool m_old_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOldUsernameContract)

#endif // OAIOldUsernameContract_H
