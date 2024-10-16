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
 * OAITeamMemberListVO.h
 *
 * Java type: com.noosh.nooshapi.vo.TeamMemberListVO
 */

#ifndef OAITeamMemberListVO_H
#define OAITeamMemberListVO_H

#include <QJsonObject>

#include "OAITeamMemberSimpleVO.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITeamMemberSimpleVO;

class OAITeamMemberListVO : public OAIObject {
public:
    OAITeamMemberListVO();
    OAITeamMemberListVO(QString json);
    ~OAITeamMemberListVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAITeamMemberSimpleVO> getResults() const;
    void setResults(const QList<OAITeamMemberSimpleVO> &results);
    bool is_results_Set() const;
    bool is_results_Valid() const;

    qint32 getStatusCode() const;
    void setStatusCode(const qint32 &status_code);
    bool is_status_code_Set() const;
    bool is_status_code_Valid() const;

    QString getStatusReason() const;
    void setStatusReason(const QString &status_reason);
    bool is_status_reason_Set() const;
    bool is_status_reason_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAITeamMemberSimpleVO> m_results;
    bool m_results_isSet;
    bool m_results_isValid;

    qint32 m_status_code;
    bool m_status_code_isSet;
    bool m_status_code_isValid;

    QString m_status_reason;
    bool m_status_reason_isSet;
    bool m_status_reason_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITeamMemberListVO)

#endif // OAITeamMemberListVO_H
