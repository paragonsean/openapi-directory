/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIShareAccessRight.h
 *
 * Specifies the mapping between this particular user and the type of access he has on shares on this device.
 */

#ifndef OAIShareAccessRight_H
#define OAIShareAccessRight_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIShareAccessRight : public OAIObject {
public:
    OAIShareAccessRight();
    OAIShareAccessRight(QString json);
    ~OAIShareAccessRight() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccessType() const;
    void setAccessType(const QString &access_type);
    bool is_access_type_Set() const;
    bool is_access_type_Valid() const;

    QString getShareId() const;
    void setShareId(const QString &share_id);
    bool is_share_id_Set() const;
    bool is_share_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access_type;
    bool m_access_type_isSet;
    bool m_access_type_isValid;

    QString m_share_id;
    bool m_share_id_isSet;
    bool m_share_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShareAccessRight)

#endif // OAIShareAccessRight_H
