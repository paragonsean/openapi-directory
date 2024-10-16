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
 * OAITeamMemberBaseInfVO.h
 *
 * Java type: com.noosh.nooshapi.vo.TeamMemberBaseInfVO
 */

#ifndef OAITeamMemberBaseInfVO_H
#define OAITeamMemberBaseInfVO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITeamMemberBaseInfVO : public OAIObject {
public:
    OAITeamMemberBaseInfVO();
    OAITeamMemberBaseInfVO(QString json);
    ~OAITeamMemberBaseInfVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getStatusCode() const;
    void setStatusCode(const qint32 &status_code);
    bool is_status_code_Set() const;
    bool is_status_code_Valid() const;

    QString getStatusReason() const;
    void setStatusReason(const QString &status_reason);
    bool is_status_reason_Set() const;
    bool is_status_reason_Valid() const;

    qint64 getTeammemberId() const;
    void setTeammemberId(const qint64 &teammember_id);
    bool is_teammember_id_Set() const;
    bool is_teammember_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_status_code;
    bool m_status_code_isSet;
    bool m_status_code_isValid;

    QString m_status_reason;
    bool m_status_reason_isSet;
    bool m_status_reason_isValid;

    qint64 m_teammember_id;
    bool m_teammember_id_isSet;
    bool m_teammember_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITeamMemberBaseInfVO)

#endif // OAITeamMemberBaseInfVO_H
