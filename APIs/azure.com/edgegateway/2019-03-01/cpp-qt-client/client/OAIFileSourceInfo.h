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
 * OAIFileSourceInfo.h
 *
 * File source details.
 */

#ifndef OAIFileSourceInfo_H
#define OAIFileSourceInfo_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFileSourceInfo : public OAIObject {
public:
    OAIFileSourceInfo();
    OAIFileSourceInfo(QString json);
    ~OAIFileSourceInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getShareId() const;
    void setShareId(const QString &share_id);
    bool is_share_id_Set() const;
    bool is_share_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_share_id;
    bool m_share_id_isSet;
    bool m_share_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFileSourceInfo)

#endif // OAIFileSourceInfo_H
