/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDistributionGroupAadGroupsDeleteResponse.h
 *
 * 
 */

#ifndef OAIDistributionGroupAadGroupsDeleteResponse_H
#define OAIDistributionGroupAadGroupsDeleteResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDistributionGroupAadGroupsDeleteResponse : public OAIObject {
public:
    OAIDistributionGroupAadGroupsDeleteResponse();
    OAIDistributionGroupAadGroupsDeleteResponse(QString json);
    ~OAIDistributionGroupAadGroupsDeleteResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAadGroupId() const;
    void setAadGroupId(const QString &aad_group_id);
    bool is_aad_group_id_Set() const;
    bool is_aad_group_id_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    qint32 getMessage() const;
    void setMessage(const qint32 &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    qint32 getStatus() const;
    void setStatus(const qint32 &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_aad_group_id;
    bool m_aad_group_id_isSet;
    bool m_aad_group_id_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    qint32 m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    qint32 m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDistributionGroupAadGroupsDeleteResponse)

#endif // OAIDistributionGroupAadGroupsDeleteResponse_H
