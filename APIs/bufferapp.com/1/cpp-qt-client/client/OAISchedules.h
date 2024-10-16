/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISchedules.h
 *
 * 
 */

#ifndef OAISchedules_H
#define OAISchedules_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISchedules : public OAIObject {
public:
    OAISchedules();
    OAISchedules(QString json);
    ~OAISchedules() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getDays() const;
    void setDays(const QList<QString> &days);
    bool is_days_Set() const;
    bool is_days_Valid() const;

    QList<QString> getTimes() const;
    void setTimes(const QList<QString> &times);
    bool is_times_Set() const;
    bool is_times_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_days;
    bool m_days_isSet;
    bool m_days_isValid;

    QList<QString> m_times;
    bool m_times_isSet;
    bool m_times_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISchedules)

#endif // OAISchedules_H
