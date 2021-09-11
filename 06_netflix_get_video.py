from enum import Enum


class ErrorCode(Enum):
    MUST_HAVE_LICENSE = 1
    CURRENT_VIEW_COUNT_OVER_FOUR = 2


def display_video(video, user):
    video = get_video(video, user)
    if video == ErrorCode.MUST_HAVE_LICENSE:
        ...  # 사용권 구매 페이지로 이동
    elif video == ErrorCode.CURRENT_VIEW_COUNT_OVER_FOUR:
        ...  # 메인 페이지로 이동
    else:
        ...


def get_video(video, user):
    if not user.has_licensed():
        return ErrorCode.MUST_HAVE_LICENSE
    elif user.license.current_view_count >= 4:
        return ErrorCode.CURRENT_VIEW_COUNT_OVER_FOUR
    return get_video_contents(video)


def get_video(video, user):
    if not user.has_licensed():
        raise Exception("사용권이 있어야만 볼 수 있습니다")
    elif user.license.current_view_count >= 4:
        raise Exception("현재 볼 수 없습니다")
    return get_video_contents(video)


def get_video_contents(video):
    ...
    return video