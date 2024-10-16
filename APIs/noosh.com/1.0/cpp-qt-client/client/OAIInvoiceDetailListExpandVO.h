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
 * OAIInvoiceDetailListExpandVO.h
 *
 * Java type: com.noosh.nooshapi.vo.InvoiceDetailListExpandVO
 */

#ifndef OAIInvoiceDetailListExpandVO_H
#define OAIInvoiceDetailListExpandVO_H

#include <QJsonObject>

#include "OAIInvoiceSimpleVO.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIInvoiceSimpleVO;

class OAIInvoiceDetailListExpandVO : public OAIObject {
public:
    OAIInvoiceDetailListExpandVO();
    OAIInvoiceDetailListExpandVO(QString json);
    ~OAIInvoiceDetailListExpandVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIInvoiceSimpleVO> getResult() const;
    void setResult(const QList<OAIInvoiceSimpleVO> &result);
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

    QList<OAIInvoiceSimpleVO> m_result;
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

Q_DECLARE_METATYPE(OpenAPI::OAIInvoiceDetailListExpandVO)

#endif // OAIInvoiceDetailListExpandVO_H
