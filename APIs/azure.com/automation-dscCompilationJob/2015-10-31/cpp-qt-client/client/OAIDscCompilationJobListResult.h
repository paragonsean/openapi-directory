/**
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-10-31
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDscCompilationJobListResult.h
 *
 * The response model for the list job operation.
 */

#ifndef OAIDscCompilationJobListResult_H
#define OAIDscCompilationJobListResult_H

#include <QJsonObject>

#include "OAIDscCompilationJob.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDscCompilationJob;

class OAIDscCompilationJobListResult : public OAIObject {
public:
    OAIDscCompilationJobListResult();
    OAIDscCompilationJobListResult(QString json);
    ~OAIDscCompilationJobListResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIDscCompilationJob> getValue() const;
    void setValue(const QList<OAIDscCompilationJob> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIDscCompilationJob> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDscCompilationJobListResult)

#endif // OAIDscCompilationJobListResult_H
