from fastapi import APIRouter
from app.api.endpoints import user, auth, company, invitation, request, quiz, question, notification

api_router = APIRouter()


api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(user.users_router, prefix="/users", tags=["users"]) # route to get all users
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(company.router, prefix="/company", tags=["company"])
api_router.include_router(company.companies_router, prefix="/companies", tags=["companies"]) # route to get all companies
api_router.include_router(invitation.router, prefix="/invite", tags=["invitation"])
api_router.include_router(request.router, prefix="/request", tags=["request"])
api_router.include_router(quiz.router, prefix="/quiz", tags=["quiz"])
api_router.include_router(question.router, prefix="/question", tags=["question"])
api_router.include_router(notification.router, prefix="/notification", tags=["notification"])