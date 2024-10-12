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
 * OAITeamTemplateExpandVO.h
 *
 * Java type: com.noosh.nooshapi.vo.TeamTemplateExpandVO
 */

#ifndef OAITeamTemplateExpandVO_H
#define OAITeamTemplateExpandVO_H

#include <QJsonObject>

#include "OAITeamTemplateDetailVO.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITeamTemplateDetailVO;

class OAITeamTemplateExpandVO : public OAIObject {
public:
    OAITeamTemplateExpandVO();
    OAITeamTemplateExpandVO(QString json);
    ~OAITeamTemplateExpandVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAITeamTemplateDetailVO getResults() const;
    void setResults(const OAITeamTemplateDetailVO &results);
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

    OAITeamTemplateDetailVO m_results;
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

Q_DECLARE_METATYPE(OpenAPI::OAITeamTemplateExpandVO)

#endif // OAITeamTemplateExpandVO_H
