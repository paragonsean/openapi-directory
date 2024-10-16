/**
 * OnSched API Utility
 * Endpoints for system utilities. e.g.Health
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIThreadPoolInfo.h
 *
 * 
 */

#ifndef OAIThreadPoolInfo_H
#define OAIThreadPoolInfo_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIThreadPoolInfo : public OAIObject {
public:
    OAIThreadPoolInfo();
    OAIThreadPoolInfo(QString json);
    ~OAIThreadPoolInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAvailableCompletionThreads() const;
    void setAvailableCompletionThreads(const qint32 &available_completion_threads);
    bool is_available_completion_threads_Set() const;
    bool is_available_completion_threads_Valid() const;

    qint32 getAvailableWorkerThreads() const;
    void setAvailableWorkerThreads(const qint32 &available_worker_threads);
    bool is_available_worker_threads_Set() const;
    bool is_available_worker_threads_Valid() const;

    qint32 getMaxCompletionThreads() const;
    void setMaxCompletionThreads(const qint32 &max_completion_threads);
    bool is_max_completion_threads_Set() const;
    bool is_max_completion_threads_Valid() const;

    qint32 getMaxWorkerThreads() const;
    void setMaxWorkerThreads(const qint32 &max_worker_threads);
    bool is_max_worker_threads_Set() const;
    bool is_max_worker_threads_Valid() const;

    qint32 getMinCompletionThreads() const;
    void setMinCompletionThreads(const qint32 &min_completion_threads);
    bool is_min_completion_threads_Set() const;
    bool is_min_completion_threads_Valid() const;

    qint32 getMinWorkerThreads() const;
    void setMinWorkerThreads(const qint32 &min_worker_threads);
    bool is_min_worker_threads_Set() const;
    bool is_min_worker_threads_Valid() const;

    qint32 getOccupiedCompletionThreads() const;
    void setOccupiedCompletionThreads(const qint32 &occupied_completion_threads);
    bool is_occupied_completion_threads_Set() const;
    bool is_occupied_completion_threads_Valid() const;

    qint32 getOccupiedWorkerThreads() const;
    void setOccupiedWorkerThreads(const qint32 &occupied_worker_threads);
    bool is_occupied_worker_threads_Set() const;
    bool is_occupied_worker_threads_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_available_completion_threads;
    bool m_available_completion_threads_isSet;
    bool m_available_completion_threads_isValid;

    qint32 m_available_worker_threads;
    bool m_available_worker_threads_isSet;
    bool m_available_worker_threads_isValid;

    qint32 m_max_completion_threads;
    bool m_max_completion_threads_isSet;
    bool m_max_completion_threads_isValid;

    qint32 m_max_worker_threads;
    bool m_max_worker_threads_isSet;
    bool m_max_worker_threads_isValid;

    qint32 m_min_completion_threads;
    bool m_min_completion_threads_isSet;
    bool m_min_completion_threads_isValid;

    qint32 m_min_worker_threads;
    bool m_min_worker_threads_isSet;
    bool m_min_worker_threads_isValid;

    qint32 m_occupied_completion_threads;
    bool m_occupied_completion_threads_isSet;
    bool m_occupied_completion_threads_isValid;

    qint32 m_occupied_worker_threads;
    bool m_occupied_worker_threads_isSet;
    bool m_occupied_worker_threads_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIThreadPoolInfo)

#endif // OAIThreadPoolInfo_H
