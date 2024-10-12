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
 * OAIScheduled_time.h
 *
 * 
 */

#ifndef OAIScheduled_time_H
#define OAIScheduled_time_H

#include <QJsonObject>

#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIScheduled_time : public OAIObject {
public:
    OAIScheduled_time();
    OAIScheduled_time(QString json);
    ~OAIScheduled_time() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getEnd() const;
    void setEnd(const QDateTime &end);
    bool is_end_Set() const;
    bool is_end_Valid() const;

    QDateTime getStart() const;
    void setStart(const QDateTime &start);
    bool is_start_Set() const;
    bool is_start_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_end;
    bool m_end_isSet;
    bool m_end_isValid;

    QDateTime m_start;
    bool m_start_isSet;
    bool m_start_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScheduled_time)

#endif // OAIScheduled_time_H
