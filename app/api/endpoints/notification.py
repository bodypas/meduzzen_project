from fastapi import APIRouter, Depends
from app.schemas.user import Result, UserResponse
from app.api.deps import get_current_user
from app.servises.notification import NotificationService, get_notification_service


router = APIRouter()


@router.get("/", response_model=Result, status_code=200, response_description="Get notifications returned")
async def get_notifications(status: bool,
                service: NotificationService = Depends(get_notification_service), 
                    current_user: UserResponse = Depends(get_current_user)) -> Result:
    notifications = await service.get_all_notifications(current_user_id=current_user.user_id, status=status)
    return Result(result={"notifications": notifications})


@router.put("/{notification_id}/status", response_model=Result, status_code=200, response_description="Notification status changed")
async def manage_notification(notification_id: int,
                    service: NotificationService = Depends(get_notification_service),
                    current_user: UserResponse = Depends(get_current_user)) -> Result:
    result = await service.manage_notification(notification_id=notification_id,
                                            current_user_id=current_user.user_id)
    return Result(result=result, message="success")
