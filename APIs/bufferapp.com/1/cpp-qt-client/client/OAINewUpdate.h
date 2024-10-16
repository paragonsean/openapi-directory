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
 * OAINewUpdate.h
 *
 * 
 */

#ifndef OAINewUpdate_H
#define OAINewUpdate_H

#include <QJsonObject>

#include "OAINewUpdate_updates_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINewUpdate_updates_inner;

class OAINewUpdate : public OAIObject {
public:
    OAINewUpdate();
    OAINewUpdate(QString json);
    ~OAINewUpdate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getBufferCount() const;
    void setBufferCount(const double &buffer_count);
    bool is_buffer_count_Set() const;
    bool is_buffer_count_Valid() const;

    double getBufferPercentage() const;
    void setBufferPercentage(const double &buffer_percentage);
    bool is_buffer_percentage_Set() const;
    bool is_buffer_percentage_Valid() const;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    QList<OAINewUpdate_updates_inner> getUpdates() const;
    void setUpdates(const QList<OAINewUpdate_updates_inner> &updates);
    bool is_updates_Set() const;
    bool is_updates_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_buffer_count;
    bool m_buffer_count_isSet;
    bool m_buffer_count_isValid;

    double m_buffer_percentage;
    bool m_buffer_percentage_isSet;
    bool m_buffer_percentage_isValid;

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;

    QList<OAINewUpdate_updates_inner> m_updates;
    bool m_updates_isSet;
    bool m_updates_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINewUpdate)

#endif // OAINewUpdate_H
