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
 * OAIUserDetailsExpandVO.h
 *
 * Java type: com.noosh.nooshapi.vo.UserDetailsExpandVO
 */

#ifndef OAIUserDetailsExpandVO_H
#define OAIUserDetailsExpandVO_H

#include <QJsonObject>

#include "OAIUserDetailsVO.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUserDetailsVO;

class OAIUserDetailsExpandVO : public OAIObject {
public:
    OAIUserDetailsExpandVO();
    OAIUserDetailsExpandVO(QString json);
    ~OAIUserDetailsExpandVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIUserDetailsVO getResult() const;
    void setResult(const OAIUserDetailsVO &result);
    bool is_result_Set() const;
    bool is_result_Valid() const;

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

    OAIUserDetailsVO m_result;
    bool m_result_isSet;
    bool m_result_isValid;

    qint32 m_status_code;
    bool m_status_code_isSet;
    bool m_status_code_isValid;

    QString m_status_reason;
    bool m_status_reason_isSet;
    bool m_status_reason_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserDetailsExpandVO)

#endif // OAIUserDetailsExpandVO_H
