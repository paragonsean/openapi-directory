/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIError.h
 *
 * 
 */

#ifndef OAIError_H
#define OAIError_H

#include <QJsonObject>

#include "OAIData.h"
#include "OAIXquery_version.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIData;

class OAIError : public OAIObject {
public:
    OAIError();
    OAIError(QString json);
    ~OAIError() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    OAIData getData() const;
    void setData(const OAIData &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    QString getErrorName() const;
    void setErrorName(const QString &error_name);
    bool is_error_name_Set() const;
    bool is_error_name_Valid() const;

    QString getExpr() const;
    void setExpr(const QString &expr);
    bool is_expr_Set() const;
    bool is_expr_Valid() const;

    QString getFormatString() const;
    void setFormatString(const QString &format_string);
    bool is_format_string_Set() const;
    bool is_format_string_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    bool isRetryable() const;
    void setRetryable(const bool &retryable);
    bool is_retryable_Set() const;
    bool is_retryable_Valid() const;

    OAIXquery_version getXqueryVersion() const;
    void setXqueryVersion(const OAIXquery_version &xquery_version);
    bool is_xquery_version_Set() const;
    bool is_xquery_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    OAIData m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    QString m_error_name;
    bool m_error_name_isSet;
    bool m_error_name_isValid;

    QString m_expr;
    bool m_expr_isSet;
    bool m_expr_isValid;

    QString m_format_string;
    bool m_format_string_isSet;
    bool m_format_string_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    bool m_retryable;
    bool m_retryable_isSet;
    bool m_retryable_isValid;

    OAIXquery_version m_xquery_version;
    bool m_xquery_version_isSet;
    bool m_xquery_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIError)

#endif // OAIError_H
