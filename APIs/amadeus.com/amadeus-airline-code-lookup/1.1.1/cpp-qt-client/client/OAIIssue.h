/**
 * Airline Code Lookup API
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIssue.h
 *
 * 
 */

#ifndef OAIIssue_H
#define OAIIssue_H

#include <QJsonObject>

#include "OAIIssue_Source.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIssue_Source;

class OAIIssue : public OAIObject {
public:
    OAIIssue();
    OAIIssue(QString json);
    ~OAIIssue() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCode() const;
    void setCode(const qint64 &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getDetail() const;
    void setDetail(const QString &detail);
    bool is_detail_Set() const;
    bool is_detail_Valid() const;

    OAIIssue_Source getSource() const;
    void setSource(const OAIIssue_Source &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    qint32 getStatus() const;
    void setStatus(const qint32 &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_detail;
    bool m_detail_isSet;
    bool m_detail_isValid;

    OAIIssue_Source m_source;
    bool m_source_isSet;
    bool m_source_isValid;

    qint32 m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIssue)

#endif // OAIIssue_H
